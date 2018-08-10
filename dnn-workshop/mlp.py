from sklearn import datasets
import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer


n_class = 3
le = LabelBinarizer()

iris = datasets.load_iris()
inputs = iris.data
outputs = le.fit_transform(iris.target)

n_input = inputs.shape()[1]

#define variables
X = tf.placeholder(tf.float64, [None, n_input], name="X")
t = tf.placeholder(tf.float64, [None, n_class], name="t")


dense1 = tf.layers.dense(X, 128, activation=tf.nn.relu, name="dense1")
dense2 = tf.layers.dense(dense1, 128, activation=tf.nn.relu, name="dense2")
output = tf.layers.dense(dense2, n_class, activation=tf.nn., name="prob_output")


loss = tf.losses.softmax_cross_entropy(t, output)
