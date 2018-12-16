import tensorflow as tf

x = tf.Variable(1., name="x")
b = tf.Variable(5., name="b")

a = tf.Variable(2. * x + tf.exp(3 * b), name="a")


init = tf.initialize_all_variables()

with tf.Session() as session:
    session.run(init)
    print(session.run(a))