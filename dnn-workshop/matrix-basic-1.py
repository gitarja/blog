import tensorflow as tf

x = tf.Variable([[1, 2], [3, 4]], name="x")
b = tf.Variable([[5, 6], [7, 8]], name="b")

dot = tf.Variable(tf.multiply(x, b), name="dot_product")
inner = tf.Variable(tf.matmul(x, b), name="inner_product")

init = tf.initialize_all_variables()
with tf.Session() as session:
    session.run(init)
    print(session.run(dot))
    print(session.run(inner))