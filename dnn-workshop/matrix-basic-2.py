import tensorflow as tf

x = tf.Variable([[7, 9], [9, 5]], name="x", dtype=tf.float64)
a = tf.Variable([[11], [2]], name="a", dtype=tf.float64)

b = tf.get_variable("b", [1, 2], dtype=tf.float64)
b = tf.matmul(tf.matrix_inverse(x), a)

init = tf.initialize_all_variables()

with tf.Session() as session:
    session.run(init)
    print(session.run(b))