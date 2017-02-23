# Lab 4 Multi-variable linear regression
import tensorflow as tf
import numpy as np

y = tf.placeholder(tf.float32, shape=[None, 1])
x = tf.placeholder(tf.float32, shape=[None, 2])

W = tf.Variable(tf.random_uniform(
    shape=[2, 1], minval=-1.0, maxval=1.0, dtype=tf.float32))
b = tf.Variable(tf.random_uniform(
    shape=[1], minval=-1.0, maxval=1.0, dtype=tf.float32))

# Hypothesis
hypothesis = tf.matmul(x, W) + b

# Simplified cost function
with tf.control_dependencies(y.shape.assert_same_rank(y)):
    cost = tf.reduce_mean(tf.square(hypothesis - y))

# Minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# Initialize variable
init = tf.global_variables_initializer()

# Launch graph
sess = tf.Session()
sess.run(init)

x_data = np.array([[1, 0], [0, 2], [3, 0], [0, 4], [5, 0]], dtype=np.float32).reshape(-1, 2)
y_data = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

for step in range(2001):
    sess.run(train, feed_dict={x: x_data, y: y_data})
    if step % 20 == 0:
        print(step, sess.run(cost, feed_dict={
              x: x_data, y: y_data}), sess.run(W), sess.run(b))
