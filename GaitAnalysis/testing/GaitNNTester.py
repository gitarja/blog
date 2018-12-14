import unittest
import tensorflow as tf
from models.GaitNN import GaitNN
from utils.Configurations import Configurations
tf.enable_eager_execution()


class MyTestCase(unittest.TestCase):
    def test_encoder(self):
        config = Configurations()
        encoder = GaitNN.Encoder(conf=config)
        decoder = GaitNN.Decoder(conf=config)
        x = tf.random_normal(shape=[5, 200, 128])
        z, z_mu, z_logvar, encoded_shape = encoder.encode(x)
        y = decoder.decode(z, encoded_shape)

        self.assertEqual(z.shape.as_list(), z_mu.shape.as_list())


if __name__ == '__main__':
    unittest.main()
