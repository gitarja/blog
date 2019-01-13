from tensorflow import keras as K
import tensorflow as tf
class GaitAE:
    class Encoder(K.models.Model):

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

            self.pool = K.layers.MaxPool1D(pool_size=conf.POOL_SIZE, padding="valid")

            self.latent_lstm = K.layers.LSTM(units=conf.LATENT_DIM,  name="latent_lstm", return_sequences=True)

        def call(self, inputs, training=None, mask=None):
            encoded = self.pool(self.encoder1(inputs))
            encoded = self.encoder2(encoded)
            encoded = self.pool(self.encoder3(encoded))
            encoded = self.pool(self.encoder4(encoded))
            encoded = self.latent_lstm(encoded)

            return encoded


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
            decoded = self.up_sample(self.decoder1(inputs))
            decoded = self.decoder2(decoded)
            decoded = self.up_sample(self.decoder3(decoded))
            decoded = self.up_sample(self.decoder4(decoded))
            decoded = self.decoder5(decoded)

            return decoded