#-*- coding: utf-8 -*-s

import numpy as np
import pandas as pd

def _map(data, exp):
    for index, row in data.iterrows():   # 获取每行的index、row
        for col_name in data.columns:
            row[col_name] = exp(row[col_name]) # 把结果返回给data
    return data

def _1map(data, exp):
    _data = [[exp(row[col_name])               # 把结果转换成2级list
             for col_name in data.columns]
             for index, row in data.iterrows()
            ]
    return _data


if __name__ == "__main__":
    inp = [{'c1':10, 'c2':100}, {'c1':11,'c2':110}, {'c1':12,'c2':120}]
    df = pd.DataFrame(inp)
    temp = _map(df, lambda ele: ele+1 )
    print temp

    _temp = _1map(df, lambda ele: ele+1)
    res_data = pd.DataFrame(_temp)         # 对2级list转换成DataFrame
    print res_data