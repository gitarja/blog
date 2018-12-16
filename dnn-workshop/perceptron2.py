import tensorflow as tf
import numpy as np


#
n_input = 2
n_output = 1

X = tf.placeholder(tf.float64, [None, n_input], name="X")
t = tf.placeholder(tf.float64, [None, n_output], name="t")


y = tf.layers.dense(X, units=n_output, activation=tf.nn.sigmoid, name="y", use_bias=True)

with tf.name_scope("Loss"):
    mse = 0.5 * tf.reduce_mean(tf.square(y - t))

train = tf.train.GradientDescentOptimizer(0.1).minimize(mse)

init = tf.global_variables_initializer()

tf.summary.scalar("loss", mse)

merge_summary_op = tf.summary.merge_all()

#write summary to path
logs_path = "./tmp/perceptron"
summary_writer = tf.summary.FileWriter(logs_path, graph=tf.get_default_graph())

#definisikan nilai
x_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
t_input = np.array([[0], [1], [1], [1]])

with tf.Session() as session:
    session.run(init)

    for epoch in range(1000):
        _, loss, summary = session.run([train, mse, merge_summary_op], feed_dict={X: x_input,
                                                        t: t_input})
        summary_writer.add_summary(summary, epoch)
        print(loss)


