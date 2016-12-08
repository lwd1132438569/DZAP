#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

inputfile = '../data/patient.xlsx'

data = pd.read_excel(inputfile)  # 导入数据

for index,row in data.iterrows():
    for col_name in data.columns:
        if(row[col_name] == u'海凤英'):
            print row

# for col_name in data.columns:
#     print col_name
# def map(data, exp):
#     for index, row in data.iterrows():   # 获取每行的index、row
#         for col_name in data.columns:
#             row[col_name] = exp(row[col_name]) # 把结果返回给data
#     return data
#
# res = map(data , lambda x : x['patient_name'])
# print res
# # def find_empi(data):
