# Lab 6 Softmax Classifier
import tensorflow as tf
import numpy as np

xy = np.loadtxt('data-04-zoo.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]
y_one_hot = tf.one_hot(y_data, 7)  # one hot
print(x_data.shape, y_data.shape)

nb_classes = 7  # 1 ~ 7

X = tf.placeholder("float", [None, 16])
Y = tf.placeholder("float", [None, 1])  # 1 ~ 7

W = tf.Variable(tf.random_normal([16, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# Softmax
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# Cross entropy cost
# cost = tf.reduce_mean(-tf.reduce_sum(Y *
#        tf.log(hypothesis), axis=1))
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    labels=y_one_hot, logits=hypothesis))

optimizer = tf.train.GradientDescentOptimizer(
    learning_rate=0.1).minimize(cost)

prediction = tf.argmax(hypothesis, 1)

# Launch graph
with tf.Session() as sess:
    # Initialize TensorFlow variables
    sess.run(tf.global_variables_initializer())

    for step in range(20001):
        sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            print(step, sess.run(cost, feed_dict={
                  X: x_data, Y: y_data}))

    # Let's see if we can predict
    pred = sess.run(prediction, feed_dict={X: x_data})
    for p, y in zip(pred, y_data):
        print("prediction: ", p, " true Y: ", y)
