#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# inputfile = '../data/sampling.xlsx'

def lr(data):
    data = pd.read_excel(data)  # 导入数据
    x = data.iloc[:,1:].as_matrix()
    y = data.iloc[:,0].as_matrix()

    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(x,y)
    # out = model.predict(x)
    accu = model.score(x,y)
    return accu

# fig, ax = plt.subplots()
# ax.scatter(y, out)
# ax.plot([y.min(), y.max()], [y.min(), y.max()], 'r', lw=4)
# ax.set_xlabel('Measured')
# ax.set_ylabel('Predicted')
# plt.show()
