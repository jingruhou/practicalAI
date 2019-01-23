import tensorflow as tf

import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

"""
    1 创建 神经网络 模型
"""
model = tf.keras.models.Sequential()  # sequential-顺序


"""
    2 添加层 (在网络图层堆栈顶部添加网络图层实例)
"""
model.add(tf.keras.layers.Dense(1, input_dim=1))

"""
    3 配置训练模型
"""
model.compile(loss='mean_squared_error', optimizer='sgd')

"""
    4 训练模型（使用固定的 epochs） - 对数据进行迭代
"""
xs = np.array([-1, 0, 1, 2, 3, 4])
ys = np.array([-3, -1, 1, 3, 5, 7])

model.fit(xs, ys, epochs=500)

"""
    5 模型预测
"""
to_predict = np.array([10, 11, 12, 13])

print(model.predict(to_predict))
