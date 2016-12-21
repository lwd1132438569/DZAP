#-*- coding: utf-8 -*-
#tf实现矩阵相乘

import tensorflow as tf

# create two matrixes

matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix1,matrix2)

sess = tf.Session()
result = sess.run(product)

print(result)
sess.close()

#another use
print '**************************'
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
