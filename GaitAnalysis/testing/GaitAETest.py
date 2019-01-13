import unittest
import tensorflow as tf
from models.GaitAE import GaitAE
from utils import Configurations


class MyTestCase(unittest.TestCase):
    def test_encoder(self):
        tf.enable_eager_execution()
        config = Configurations
        encoder = GaitAE.Encoder(conf=config)
        decoder = GaitAE.Decoder(conf=config)
        x = tf.random_normal(shape=[5, 200, 1])
        z = encoder(x)
        y = decoder(z)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()