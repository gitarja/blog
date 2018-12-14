import unittest
import tensorflow as tf
from models.GaitNN import Encoder
from utils.Configurations import Configurations
tf.enable_eager_execution()


class MyTestCase(unittest.TestCase):
    def test_encoder(self):
        config = Configurations()
        encoder = Encoder(conf=config)
        x = tf.random_normal(shape=[1, 40, 128])
        z, z_mu, z_logvar = encoder.encode(x)

        self.assertEqual(z.shape.as_list(), z_mu.shape.as_list())


if __name__ == '__main__':
    unittest.main()
