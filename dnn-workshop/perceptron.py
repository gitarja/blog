import tensorflow as tf
import numpy as np


#
n_input = 2
n_output = 1

X = tf.placeholder(tf.float64, [None, n_input], name="X")
W = tf.get_variable(name="W", shape=[n_input, n_output], initializer=tf.random_uniform_initializer, dtype=tf.float64)
t = tf.placeholder(tf.float64, [None, n_output], name="y")

y = tf.sigmoid(tf.matmul(X, W))

mse = 0.5 * tf.reduce_mean(tf.square(y - t))

train = tf.train.GradientDescentOptimizer(0.1).minimize(mse)

init = tf.initialize_all_variables()


#definisikan nilai
x_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
t_input = np.array([[0], [1], [1], [1]])

with tf.Session() as session:
    session.run(init)

    for epoch in range(100):
        _, loss = session.run([train, mse], feed_dict={X: x_input,
                                                        t: t_input})
        print(loss)


