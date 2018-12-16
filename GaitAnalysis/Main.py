from utils.Generator import DataGenerator
from models.GaitNN import GaitNN
from utils import Configurations
import tensorflow as tf
from tensorflow.contrib import summary
import glob

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
encoder = GaitNN.Encoder(conf)
decoder = GaitNN.Decoder(conf)
optimizer = tf.train.AdamOptimizer(learning_rate=conf.LR)



"Start training process"
with summary_writer.as_default(), summary.always_record_summaries(), tfe.restore_variables_on_create(
          tf.train.latest_checkpoint(conf.CHECKPOINT_DIR)):
    for i in range(conf.NUM_ITER):
        global_step = tf.train.get_or_create_global_step()
        loss = 0
        for batch_index in range(data_num):
            with tf.GradientTape() as tape:
                X = generator.getFlow(batch_index)
                x = tf.constant(X, dtype=tf.float32)
                z, z_mu, z_logvar, encoded_shape = encoder.encode(x)
                y = decoder.decode(z, encoded_shape)
                loss += vae_loss(x, y, z_mu, z_logvar)

                "Do backprop"
                grads = tape.gradient(loss, (encoder.trainable_variables, decoder.trainable_variables))
                optimizer.apply_gradients(zip(grads[0], encoder.trainable_variables))
                optimizer.apply_gradients(zip(grads[1], decoder.trainable_variables))

        avg_loss = loss / data_num
        summary.scalar("loss", avg_loss, step=i)
        print("Iteration %d, training_loss: %f" % (i, avg_loss))

        all_variables = (
                encoder.variables + decoder.variables
                + optimizer.variables() + [global_step])
        saver = tfe.Saver(all_variables)
        saver.save(
            conf.CHECKPOINT_PREFIX, global_step=global_step)




