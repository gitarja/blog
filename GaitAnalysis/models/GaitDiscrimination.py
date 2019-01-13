import tensorflow as tf
from tensorflow import keras as K

class GaitDiscriminator(K.models.Model):

    class Discriminator(K.models.Model):
        def __init__(self, conf):
            super().__init__()

            self.dense1 = K.layers.Dense(units=conf.DISC_DENSE_UNITS[0], activation="relu")
            self.dense2 = K.layers.Dense(units=conf.DISC_DENSE_UNITS[1], activation="relu")
            self.dense3 = K.layers.Dense(units=1, activation="linear")

            self.drop_out = K.layers.Dropout(0.3)

            self.flatten = K.layers.Flatten()


        def call(self, inputs, training=None, mask=None):
            y = self.dense1(self.flatten(inputs))
            y = self.dense2(self.drop_out(y))
            y = self.dense3(y)

            return y

    class DeepDiscriminator(K.models.Model):
        def __init__(self, conf):
            super().__init__()

            self.dense1 = K.layers.Dense(units=conf.DISC_DENSE_UNITS[0], activation="relu")
            self.dense2 = K.layers.Dense(units=conf.DISC_DENSE_UNITS[1], activation="relu")
            self.dense3 = K.layers.Dense(units=conf.DISC_DENSE_UNITS[1], activation="relu")
            self.dense4 = K.layers.Dense(units=conf.DISC_DENSE_UNITS[1], activation="relu")
            self.dense5 = K.layers.Dense(units=1, activation="linear")

            self.drop_out = K.layers.Dropout(0.3)

            self.flatten = K.layers.Flatten()

        def call(self, inputs, training=None, mask=None):
            y = self.dense1(self.flatten(inputs))
            y = self.dense2(self.drop_out(y))
            y = self.dense3(self.drop_out(y))
            y = self.dense4(self.drop_out(y))
            y = self.dense5(y)

            return y
