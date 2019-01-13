from utils.Generator import DataGenerator
# from models.GaitNN import GaitNN
from models.GaitAE import GaitAE
from utils import Configurations
import tensorflow as tf
from tensorflow.contrib import summary
import glob
import math

tfe = tf.contrib.eager
tf.enable_eager_execution()


"Define VAE loss"

def vae_loss(y_true, y_pred, mean, logvar):

        #recontstruction loss
        reconstructionLoss = tf.reduce_sum(tf.square(y_true - y_pred))
        #kl differgence with Gaussian
        klLoss = -0.5 * tf.reduce_sum(1 + logvar - tf.square(mean) - tf.exp(logvar), axis=-1)

        return tf.reduce_mean(reconstructionLoss + klLoss)

"Defining configuration, generator and summary writer"
conf = Configurations

generator = DataGenerator(conf.BATCH_SIZE, conf.FILE_PATH, conf.T)

summary_writer = summary.create_file_writer(conf.TENSORBOARD_DIR)
"Number of dataset"
data_num = int(len(glob.glob("".join([conf.FILE_PATH, "*.txt"]))) / conf.BATCH_SIZE)

"Define Model and Optimizer"
encoder = GaitAE.Encoder(conf)
decoder = GaitAE.Decoder(conf)
optimizer = tf.train.AdamOptimizer(learning_rate=conf.LR)

check_point = tf.train.Checkpoint(optimizer=optimizer, encoder=encoder, decoder=decoder, global_step=tf.train.get_or_create_global_step())

manager = tf.contrib.checkpoint.CheckpointManager(
    check_point, directory=conf.CHECKPOINT_DIR, max_to_keep=20)
status = check_point.restore(manager.latest_checkpoint)

"Start training process"
with summary_writer.as_default(), summary.always_record_summaries():
    for i in range(conf.NUM_ITER):
        global_step = tf.train.get_or_create_global_step()
        loss = 0
        for batch_index in range(data_num):
            X = generator.getFlow(batch_index)
            x = tf.constant(X, dtype=tf.float32)
            with tf.GradientTape() as tape:
                # z, z_mu, z_logvar, encoded_shape = encoder.encode(x)
                # y = decoder.decode(z, encoded_shape)
                # entropy = vae_loss(x, y, z_mu, z_logvar)
                z = encoder(x)
                y = decoder(z)
                entropy = tf.losses.mean_squared_error(labels=x, predictions=y)

                loss += entropy

                "Do backprop"
            grads = tape.gradient(entropy, (encoder.trainable_variables, decoder.trainable_variables))
            optimizer.apply_gradients(zip(grads[0], encoder.trainable_variables))
            optimizer.apply_gradients(zip(grads[1], decoder.trainable_variables))

        avg_loss = loss / data_num
        summary.scalar("loss", avg_loss, step=i)
        print("Iteration %d, training_loss: %f" % (i, avg_loss))
        if (i+1) % 200 == 0:
            optimizer._lr = optimizer._lr * math.sqrt(0.3)

        if (i+1) % 50 == 0:
            manager.save()





