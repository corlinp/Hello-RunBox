# Simple hello world using TensorFlow
from __future__ import print_function
import tensorflow as tf

hello = tf.constant('Hello, Tenzar RunBox!')
sess = tf.Session()
print(sess.run(hello))
