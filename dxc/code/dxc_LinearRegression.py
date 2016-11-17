#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

def lr():
    x = data[0]
    y = data[1]

    model = LinearRegression()
    model.fit(x,y)
    out = model.predict(x)
    return out

# fig, ax = plt.subplots()
# ax.scatter(y, out)
# ax.plot([y.min(), y.max()], [y.min(), y.max()], 'r', lw=4)
# ax.set_xlabel('Measured')
# ax.set_ylabel('Predicted')
# plt.show()
