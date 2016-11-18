# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# 参数初始化
# inputfile = '../data/sampling.xlsx'
def nn(inputfile):
    data = pd.read_excel(inputfile)  # 导入数据

    x = data.iloc[:, 1:].as_matrix().astype(int)
    y = data.iloc[:, 0].as_matrix().astype(int)

    model = Sequential()
    model.add(Dense(26, input_dim=26))
    model.add(Activation('linear'))

    model.add(Dense(26))
    model.add(Activation('linear'))

    model.add(Dense(1))
    model.add(Activation('linear'))

    model.compile(loss='mean_squared_error', optimizer="rmsprop", metrics=["accuracy"])

    hist = model.fit(x, y, batch_size=5, nb_epoch=100, shuffle=True, verbose=0, validation_split=0.2)

    out = model.predict(x, batch_size=5, verbose=0)

    # print '#####################'
    # print out
    score = model.evaluate(x, y, batch_size=5)
    return score

# fig, ax = plt.subplots()
# ax.scatter(y, out)
# ax.plot([y.min(), y.max()], [y.min(), y.max()], 'g', lw=4)
# ax.set_xlabel('Measured')
# ax.set_ylabel('Predicted')
# plt.show()