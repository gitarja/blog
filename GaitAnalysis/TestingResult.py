from models.GaitNN import GaitNN
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
encoder = GaitNN.Encoder(conf)
decoder = GaitNN.Decoder(conf)

x = tf.random.uniform(shape=(1, conf.T, conf.UNIT))
z, z_mu, z_logvar, encoded_shape = encoder.encode(x)
y = decoder.decode(z, encoded_shape)
all_variables = (encoder.variables + decoder.variables)
saver = tfe.Saver(all_variables)
saver.restore(tf.train.latest_checkpoint(conf.CHECKPOINT_DIR))

"Test the model"
X = generator.getFlow(0)
x = tf.constant(X, dtype=tf.float32)
z, z_mu, z_logvar, encoded_shape = encoder.encode(x)
y = decoder.decode(z, encoded_shape)

loss = tf.reduce_mean(tf.square(x - y))
print(loss)
cross_loss = np.correlate(X[0].reshape(200, ), y.numpy()[0].reshape(200, ))
print(cross_loss)

plt.figure(1)
plt.plot(X[0])
plt.plot(y.numpy()[0])

plt.show()

