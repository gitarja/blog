from sklearn import datasets
import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer



le = LabelBinarizer()
logs_path = "./tmp/mlp"
iris = datasets.load_iris()
x_input = iris.data
t_input = le.fit_transform(iris.target)

n_class = 3
n_input = x_input.shape[1]

#define variables
X = tf.placeholder(tf.float64, [None, n_input], name="X")
t = tf.placeholder(tf.float64, [None, n_class], name="t")


dense1 = tf.layers.dense(X, 128, activation=tf.nn.relu, name="dense1")
dense2 = tf.layers.dense(dense1, 128, activation=tf.nn.relu, name="dense2")
output = tf.layers.dense(dense2, n_class, activation=None, name="prob_output")

with tf.name_scope("Loss"):
    entropy = tf.losses.softmax_cross_entropy(t, output)

with tf.name_scope("Accuracy"):
    acc = tf.equal(tf.arg_max(t, 1), tf.arg_max(output, 1))
    acc = tf.reduce_mean(tf.cast(acc, tf.float32))

with tf.name_scope("GD"):
    train = tf.train.GradientDescentOptimizer(0.01).minimize(entropy)

init = tf.global_variables_initializer()

#create summary
tf.summary.scalar("loss", entropy)
tf.summary.scalar("accuracy", acc)

merge_summary_op = tf.summary.merge_all()

#write summary to path
summary_writer = tf.summary.FileWriter(logs_path, graph=tf.get_default_graph())

with tf.Session() as session:
    session.run(init)

    for epoch in range(1000):
        _, loss, summary = session.run([train, entropy, merge_summary_op], feed_dict={X: x_input, t:t_input})
        summary_writer.add_summary(summary, epoch)

        print(loss)