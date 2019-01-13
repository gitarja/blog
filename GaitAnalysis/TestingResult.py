# from models.GaitNN import GaitNN
import scipy.fftpack
from models.GaitAE import GaitAE
from utils import Configurations
from utils.Generator import DataGenerator
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
tfe = tf.contrib.eager
tf.enable_eager_execution()

conf = Configurations

generator = DataGenerator(1, conf.FILE_PATH, conf.T)
"Define Model"
# encoder = GaitNN.Encoder(conf)
# decoder = GaitNN.Decoder(conf)



encoder = GaitAE.Encoder(conf)
decoder = GaitAE.Decoder(conf)



check_point = tf.train.Checkpoint(encoder=encoder, decoder=decoder, global_step=tf.train.get_or_create_global_step())

manager = tf.contrib.checkpoint.CheckpointManager(
    check_point, directory=conf.CHECKPOINT_DIR, max_to_keep=20)
status = check_point.restore(manager.latest_checkpoint)

for i in range(50):
    "Test the model"
    X = generator.getFlow(i)
    x = tf.constant(X, dtype=tf.float32)
    # z, z_mu, z_logvar, encoded_shape = encoder.encode(x)
    # y = decoder.decode(z, encoded_shape)

    z = encoder(x)
    y = decoder(z)

    loss = tf.reduce_mean(tf.square(x - y))
    # print(loss)
    # cross_loss = np.correlate(X[0].reshape(200, ), y.numpy()[0].reshape(200, ))
    # print(cross_loss)

    fig, ax = plt.subplots( nrows=1, ncols=1 )


    for j in range(32):
        latent = z.numpy()[0, :, j]
        latentFFT = scipy.fftpack.fft(latent)
        xf = np.linspace(0.0, 1.0 / (2.0 * conf.HZT), 25 / 2)
        # zMax = np.max(latent)
        # zMin = np.min(latent)
        # ax.plot((latent - zMin) / (zMax - zMin))
        ax.plot(xf, 2.0/25 * np.abs(latentFFT[0:int(25/2)]))
        # ax.plot(np.average(latent, axis=-1))
        # ax.plot(X[0])
        # ax.plot(y.numpy()[0])

    # ax.plot(np.average(z.numpy()[0, :, :], axis=-1))
    fig.savefig("".join([conf.DISC_IMG_LATENT, "\\", generator.filename, "_latent_fft.png"]))  # save the figure to file
    plt.close(fig)
    # plt.plot(X[0])
    # plt.plot(y.numpy()[0])

    # plt.show()

