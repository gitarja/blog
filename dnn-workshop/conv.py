import tensorflow as tf

(X_train, t_train), (X_test, t_test) = tf.keras.datasets.cifar10.load_data()



n_class = 10


num_data = X_train.shape[0]
img_channel = X_train.shape[3]
filters = [128, 256, 512, 512]
mb = 10
total_batch = int(num_data/mb)
num_itr = 100



#define variable
X = tf.placeholder(tf.float32, [None, X_train.shape[1], X_train.shape[2], img_channel], name="input")
y = tf.placeholder(tf.uint8, [None, 1], name="y")
y_hot = tf.one_hot(y, n_class)

cnn1 = tf.layers.conv2d(X, filters=filters[0], kernel_size=3, strides=2, name="cnn1")
pool1 = tf.layers.max_pooling2d(cnn1, pool_size=2, strides=1, name="pool1")
cnn2 = tf.layers.conv2d(pool1, filters=filters[1], kernel_size=3, strides=2, name="cnn2")
pool2 = tf.layers.max_pooling2d(cnn2, pool_size=2, strides=1, name="pool2")
cnn3 = tf.layers.conv2d(pool2, filters=filters[2], kernel_size=3, strides=2, name="cnn3")
pool3 = tf.layers.max_pooling2d(cnn3, pool_size=2, strides=1, name="pool3")
input_dense = tf.layers.flatten(pool3, name="input_dense")
dense1 = tf.layers.dense(input_dense, units=filters[3], activation=tf.nn.relu, name="dense1")
output = tf.layers.dense(dense1, units=n_class, name="output")

entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=output, labels=y_hot))

train = tf.train.AdamOptimizer(0.001).minimize(entropy)

init = tf.global_variables_initializer()


with tf.Session() as session:
    session.run(init)
    avg_cost = 0.
    for itr in range(num_itr):
        for step in range(total_batch):
            X_batch = X_train[step*mb:(step+1)*mb]
            t_batch = t_train[step*mb:(step+1)*mb]
            _, loss = session.run([train, entropy], feed_dict={X: X_batch, y: t_batch})
            avg_cost += loss / total_batch

    




