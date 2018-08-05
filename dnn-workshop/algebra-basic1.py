import tensorflow as tf

# x = tf.Variable(1, name="x")
# b = tf.Variable(5, name="b")

x = tf.Variable([1, 2, 3], name="x")
b = tf.Variable([2, 3, 4], name="b")

a = tf.Variable(tf.multiply(x, b) + tf.pow(b, 2), name="a")


init = tf.initialize_all_variables()

with tf.Session() as session:
    session.run(init)
    print(session.run(a))