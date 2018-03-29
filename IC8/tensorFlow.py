import tensorflow as tf
import numpy
from numpy import *
sess = tf.InteractiveSession()
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))



a = range(16)
a = reshape(a,(4,4))
print(a)
b = range(16)
b = reshape(b,(4,4))
print(b)
c = range(16)
c = reshape(c,(4,4))
print(c)

d = tf.matmul(a,b)
print(d)

y = tf.matmul(
    a,
    b,
    transpose_a=False,
    transpose_b=False,
    adjoint_a=False,
    adjoint_b=False,
    a_is_sparse=False,
    b_is_sparse=False,
    name=None
)
print(y)
z = tf.constant([[1, 2], [3, 4], [5, 6]])
shuff = tf.random_shuffle(z)
z = tf.Print(z,[z],message="Matrix: ")
z.eval()
#a has two elements
a = tf.constant([35,6])
#b has two elements
b = tf.constant([4,59])
#c has two elements
c = tf.constant([95,97])
#d is the square
d = tf.square(a)
#e is the add operation
e = tf.add(d,b)

f=tf.multiply(e,c)
print(f)
# Build a graph.
t1 = tf.constant(5.0)
t2 = tf.constant(6.0)
t3 = t1 * t2

# Launch the graph in a session.
sess = tf.Session()

# Evaluate the tensor `c`.
print(sess.run(f))
