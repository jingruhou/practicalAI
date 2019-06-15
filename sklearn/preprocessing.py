from sklearn import preprocessing
import numpy as np

x_train = np.array([[1., -1, 2.],
                   [2., 0., 0.],
                   [0., 1., -1.]])
x_scaled = preprocessing.scale(x_train)

print(x_scaled)

mean = x_scaled.mean(axis=0)
print(mean)

std = x_scaled.std(axis=0)
print(std)