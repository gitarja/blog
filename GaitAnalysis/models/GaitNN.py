from tensorflow import keras as K
import tensorflow as tf



class GaitNN:
    class Encoder(K.models.Model):

        def sampling(self, args):
            """Reparameterization trick by sampling fr an isotropic unit Gaussian.
                # Arguments:
                    args (tensor): mean and log of variance of Q(z|X)
                # Returns:
                    z (tensor): sampled latent vector
            """
            z_mean, z_logvar = args
            batch = tf.shape(z_mean)[0]
            dim = tf.shape(z_mean)[-1]

            # sampling z = mean + exp(logvar) * eps
            epsilon = tf.random_normal(shape=[batch, dim])
            z = z_mean + tf.exp(0.5 * z_logvar) * epsilon
            return z

        def __init__(self, conf):
            super().__init__()
            self.encoder1 = K.layers.Conv1D(name="encoder1", padding="same", activation="relu",
                                            kernel_size=conf.KERNEL_SIZE[0], filters=conf.FILTER_SIZE[0])
            self.encoder2 = K.layers.Conv1D(name="encoder2", padding="same", activation="relu",
                                            kernel_size=conf.KERNEL_SIZE[1], filters=conf.FILTER_SIZE[1])
            self.encoder3 = K.layers.Conv1D(name="encoder3", padding="same", activation="relu",
                                            kernel_size=conf.KERNEL_SIZE[2], filters=conf.FILTER_SIZE[2])
            self.encoder4 = K.layers.Conv1D(name="encoder4", padding="same", activation="relu",
                                            kernel_size=conf.KERNEL_SIZE[2], filters=conf.FILTER_SIZE[3])

            self.dense_mu = K.layers.Dense(name="z_mu", units=conf.LATENT_DIM, activation="linear")
            self.dense_logvar = K.layers.Dense(name="z_var", units=conf.LATENT_DIM, activation="linear")

            self.pool = K.layers.MaxPool1D(pool_size=conf.POOL_SIZE, padding="valid")

            self.sampling_func = K.layers.Lambda(self.sampling, output_shape=[conf.LATENT_DIM, ], name="z")
            self.flatten = K.layers.Flatten()

        def call(self, inputs, training=None, mask=None):
            encoded = self.pool(self.encoder1(inputs))
            encoded = self.encoder2(encoded)
            encoded = self.pool(self.encoder3(encoded))
            encoded = self.pool(self.encoder4(encoded))

            encoded_shape = tf.shape(encoded)
            z_mu = self.dense_mu(self.flatten(encoded))
            z_logvar = self.dense_logvar(self.flatten(encoded))

            z = self.sampling_func([z_mu, z_logvar])

            return z, z_mu, z_logvar, encoded_shape

        def encode(self, x):
            return self(x)

    class Decoder(K.models.Model):

        def __init__(self, conf):
            super().__init__()
            self.decoder1 = K.layers.Conv1D(name="decoder1", padding="same", activation="relu",
                                            kernel_size=conf.KERNEL_SIZE[2], filters=conf.FILTER_SIZE[3])
            self.decoder2 = K.layers.Conv1D(name="decoder2", padding="same", activation="relu",
                                            kernel_size=conf.KERNEL_SIZE[2], filters=conf.FILTER_SIZE[2])
            self.decoder3 = K.layers.Conv1D(name="decoder3", padding="same", activation="relu",
                                            kernel_size=conf.KERNEL_SIZE[1], filters=conf.FILTER_SIZE[1])
            self.decoder4 = K.layers.Conv1D(name="decoder4", padding="same", activation="relu",
                                            kernel_size=conf.KERNEL_SIZE[0], filters=conf.FILTER_SIZE[0])
            self.decoder5 = K.layers.Conv1D(name="decoder5", padding="same", activation="relu",
                                            kernel_size=conf.KERNEL_SIZE[2], filters=conf.UNIT)



            self.up_sample = K.layers.UpSampling1D(size=conf.POOL_SIZE)

        def call(self, inputs, training=None, mask=None):
            z = K.layers.Dense(activation="relu", units=inputs[1][1] * inputs[1][2])(inputs[0])
            z = tf.reshape(z, inputs[1])
            decoded = self.up_sample(self.decoder1(z))
            decoded = self.decoder2(decoded)
            decoded = self.up_sample(self.decoder3(decoded))
            decoded = self.up_sample(self.decoder4(decoded))
            decoded = self.decoder5(decoded)
            return decoded

        def decode(self, x, encoded_shape):
            return self([x, encoded_shape])
