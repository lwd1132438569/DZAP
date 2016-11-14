#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt 

inputfile = '../data/sampling.xlsx'
data = pd.read_excel(inputfile) #导入数据

x = data.iloc[:,1:].as_matrix()
y = data.iloc[:,0].as_matrix()

print x
print '**********************************' 
print y

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
print model.coef_
print model.score(x,y)
print '***********************************'
out = model.predict(x)

fig, ax = plt.subplots()
ax.scatter(y, out)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'r', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
