import tensorflow.contrib.keras as K
import tensorflow as tf

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

        #sampling z = mean + exp(logvar) * eps
        epsilon = tf.random_normal(shape=[batch, dim])
        z = z_mean + tf.exp(0.5 * z_logvar) * epsilon
        return z

    def __init__(self, conf):
        super().__init__()
        self.encoder1 = K.layers.Conv1D(name="encoder1", filters=conf.filter_size[0], kernel_size=conf.kernel_size[0])
        self.encoder2 = K.layers.Conv1D(name="encoder2", filters=conf.filter_size[0], kernel_size=conf.kernel_size[0])
        self.encoder3 = K.layers.Conv1D(name="encoder3", filters=conf.filter_size[1], kernel_size=conf.kernel_size[1])
        self.encoder4 = K.layers.Conv1D(name="encoder3", filters=conf.filter_size[1], kernel_size=conf.kernel_size[1])

        self.dense_mu = K.layers.Dense(name="z_mu", units=conf.latent_dim)
        self.dense_logvar = K.layers.Dense(name="z_var", units=conf.latent_dim)

        self.pool = K.layers.MaxPool1D(pool_size=conf.pool_size, padding="valid", strides=conf.strides)

        self.sampling_func = K.layers.Lambda(self.sampling, output_shape=[conf.latent_dim, ], name="z")

    def call(self, inputs, training=None, mask=None):
        decoded = self.pool(self.encoder1(inputs))
        decoded = self.encoder2(decoded)
        decoded = self.pool(self.encoder3(decoded))
        decoded = self.pool(self.encoder4(decoded))

        z_mu = self.dense_mu(decoded)
        z_logvar = self.dense_logvar(decoded)

        z = self.sampling_func([z_mu, z_logvar])

        return z, z_mu, z_logvar

    def encode(self, x):
        return self(x)


