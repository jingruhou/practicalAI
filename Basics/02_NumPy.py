import numpy as np

#  设置种子以获得可重复性
np.random.seed(seed=1234)

"""
    1   Numpy Basics
"""

x = np.array(6)

print("x:", x)
print("x ndim: ", x.ndim)
print("x shape: ", x.shape)
print("x size: ", x.size)
print("x dtype: ", x.dtype)

print("\n")

x = np.array([1.3, 2.2, 1.7])
print("x: ", x)
print("x ndim: ", x.ndim)
print("x shape: ", x.shape)
print("x size: ", x.size)
print("x dtype: ", x.dtype)

print("\n")

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("x: \n", x)
print("x ndim: ", x.ndim)
print("x shape: ", x.shape)
print("x size: ", x.size)
print("x dtype: ", x.dtype)

print("\n")

#  函数
print("np.zeros((2,2)):\n", np.zeros((2, 2)))
print("np.ones((2,2)):\n", np.ones((2, 2)))
print("np.eye((2)):\n", np.eye(2))
print("np.random.random((2,2)):\n", np.random.random((2, 2)))

print("\n")

"""
    2   Indexing
"""

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(x)
print("x column 1: ", x[:, 1])
print("x row 0: ", x[0, :])
print("x rows 0,1,2 & cols 1,2: \n", x[:3, 1:3])

print("\n")

print(x)
rows_to_get = np.arange(len(x))
print("row_to_get: ", rows_to_get)

cols_to_get = np.array([0, 2, 1])
print("cols_to_get: ", cols_to_get)
print("indexed values: ", x[rows_to_get, cols_to_get])

print("\n")

x = np.array([[1, 2], [3, 4], [5, 6]])
print("x:\n", x)
print("x > 2:\n", x > 2)
print("x[x > 2]:\n", x[x > 2])

print("\n")

"""
    3   Array math
"""

#  基本运算
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[1, 2], [3, 4]], dtype=np.float64)

print("x + y:\n", np.add(x, y))
print("x - y:\n", np.subtract(x, y))
print("x * y:\n", np.multiply(x, y))

print("\n")

#  Dot product - 点乘
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
b = np.array([[7, 8], [9, 10], [11, 12]], dtype=np.float64)
print(a.dot(b))

print("\n")

# Sum across a dimension - 垮维度求和
x = np.array([[1, 2], [3, 4]])
print(x)
print("sum all: ", np.sum(x))  # 添加所有的元素
print("sum by col: ", np.sum(x, axis=0))  # 在每列中添加数字
print("sum by row: ", np.sum(x, axis=1))  # 再每行中添加数字

print("\n")

# Transposing
print("x:\n", x)
print("x.T\n", x.T)

print("\n")

"""
    4   Advanced
"""

# tile
x = np.array([[1, 2], [3, 4]])
y = np.array([5, 6])
addent = np.tile(y, (len(x), 1))
print("addent:\n", addent)
z = x + addent
print("z:\n", z)

print("\n")

# Broadcasting
x = np.array([[1, 2], [3, 4]])
y = np.array([5, 6])
z = x + y
print("z:\n", z)

print("\n")

x = np.array([[1, 2], [3, 4], [5, 6]])
print(x)
print("x.shape: ", x.shape)
y = np.reshape(x, (2, 3))
print("y.shape: ", y.shape)
print("y: \n", y)

print("\n")

# Removing dimensions 删除维度
x = np.array([[[1, 2, 1]], [[2, 2, 3]]])
print("x.shape: ", x.shape)
y = np.squeeze(x, 1)
print("y.shape: ", y.shape)
print("y:\n", y)

print("\n")

# Adding dimensions 增加维度
x = np.array([[1, 2, 1], [2, 2, 3]])
print("x.shape: ", x.shape)
y = np.expand_dims(x, 1)  # expand dim 1
print("y.shape: ", y.shape)
print("y: \n", y)