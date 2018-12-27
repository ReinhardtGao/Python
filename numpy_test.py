import numpy as np

'''
a = np.random.randn(3, 3)
b = np.random.randn(3, 1)
c = a * b
# print(c)

a = np.random.randn(12288, 150)  # a.shape = (12288, 150)
b = np.random.randn(150, 45)  # b.shape = (150, 45)
c = np.dot(a, b)
# print(c)
# print(c.shape)
'''

A = np.random.randn(4, 3)
B = np.sum(A, axis=1, keepdims=True)
print(B.shape)

