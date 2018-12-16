import unittest
import tensorflow as tf
from models.GaitNN import GaitNN
from utils import Configurations



class MyTestCase(unittest.TestCase):
    def test_encoder(self):
        tf.enable_eager_execution()
        config = Configurations
        encoder = GaitNN.Encoder(conf=config)
        decoder = GaitNN.Decoder(conf=config)
        x = tf.random_normal(shape=[5, 200, 1])
        z, z_mu, z_logvar, encoded_shape = encoder.encode(x)
        y = decoder.decode(z, encoded_shape)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
