from utils.DiscriminatorGenerator import DataGenerator
# from models.GaitNN import GaitNN
from models.GaitAE import GaitAE
from models.GaitDiscrimination import GaitDiscriminator
from utils import Configurations
import tensorflow as tf
from tensorflow.contrib import summary
import glob
import math

tfe = tf.contrib.eager
tf.enable_eager_execution()

"Defining configuration, generator and summary writer"
val_loss_th = 1e+13
conf = Configurations

generator_train = DataGenerator(file_path=conf.TRAIN_FILE_PATH, dataset_path=conf.FILE_PATH, T=conf.T)
generator_val = DataGenerator(file_path=conf.VAL_FILE_PATH, dataset_path=conf.FILE_PATH, T=conf.T)

summary_writer = summary.create_file_writer(conf.DISC_TENSORBOARD_DIR)

"Define Model and Optimizer"
encoder = GaitAE.Encoder(conf)
discriminator = GaitDiscriminator.DeepDiscriminator(conf)
optimizer = tf.train.AdamOptimizer(learning_rate=conf.DIC_LR)

"Restore pre-trained model"
pre_trained_check_point = tf.train.Checkpoint(encoder=encoder)
pre_trained_check_point.restore(tf.train.latest_checkpoint(conf.CHECKPOINT_DIR))

"check point"
check_point = tf.train.Checkpoint(optimizer=optimizer, encoder=encoder, discriminator=discriminator,
                                  global_step=tf.train.get_or_create_global_step())

manager = tf.contrib.checkpoint.CheckpointManager(
    check_point, directory=conf.DISC_CHECKPOINT_DIR, max_to_keep=20)
# status = check_point.restore(manager.latest_checkpoint)

"Start training process"
with summary_writer.as_default(), summary.always_record_summaries():
    for i in range(conf.DIC_NUM_ITER):
        global_step = tf.train.get_or_create_global_step()
        "Training"
        X, t = generator_train.getFlow()
        x = tf.constant(X, dtype=tf.float32)
        t = tf.constant(t, dtype=tf.float32)
        with tf.GradientTape() as tape:
            # z = encoder(x)
            y = discriminator(x)
            loss = tf.losses.mean_squared_error(labels=t, predictions=y)
            "Do backprop"
        # grads = tape.gradient(loss, (discriminator.trainable_variables, encoder.trainable_variables))
        grads = tape.gradient(loss, discriminator.trainable_variables)
        optimizer.apply_gradients(zip(grads, discriminator.trainable_variables))
        # optimizer.apply_gradients(zip(grads[1], encoder.trainable_variables))

        "Validation"
        X, t = generator_val.getFlow()
        x = tf.constant(X, dtype=tf.float32)
        t = tf.constant(t, dtype=tf.float32)
        # z = encoder(x)
        y = discriminator(x)
        val_loss = tf.losses.mean_squared_error(labels=t, predictions=y)

        summary.scalar("loss", loss, step=i)
        summary.scalar("val_loss", val_loss, step=i)
        print("Iteration %d, training loss: %f, validation loss %f" % (i, loss, val_loss))
        if (i + 1) % 150 == 0:
            optimizer._lr = optimizer._lr * math.sqrt(0.5)

        if val_loss_th > val_loss:
            manager.save()
            val_loss_th = val_loss
