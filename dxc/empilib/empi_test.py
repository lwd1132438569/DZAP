#-*- coding: utf-8 -*-

#找重复值的SQL
#SELECT z.patient_name name , COUNT(z.patient_name) num FROM `zmap_r_patient` as z GROUP BY z.patient_name HAVING COUNT(z.patient_name) > 1 order by num desc;

import pandas as pd
import matplotlib.pyplot as plt
import pymysql

# inputfile = '../data/patient.xlsx'
#
# data = pd.read_excel(inputfile)  # 导入数据
#
# for index,row in data.iterrows():
#     for col_name in data.columns:
#         if(row[col_name] == u'海凤英'):
#             print row
#***************查找所有名字相同的字段*********************************
# conn = pymysql.connect(host = '139.196.198.56', user='root' , passwd='Jth2016', db = 'zmap_empi', charset = 'utf8')
# cur = conn.cursor()
#
# # cur.execute("select * from zmap_r_patient limit 10")
# query = "SELECT * from (SELECT z.patient_name name , COUNT(z.patient_name) the_sum FROM zmap_r_patient as z GROUP BY z.patient_name HAVING COUNT(z.patient_name) > 1 AND name != '') as a,zmap_r_patient b where b.patient_name = a.name ORDER BY a.name"
# cur.execute(query)
# result = cur.fetchall()
# for i in range(48,75):
#         print result[i][0],result[i][1]
#*********************************************************************

#**********************测试输入一个名字作为查询条件，输出其所有字段***************************************************
import pymysql

name = '下建芳'
conn = pymysql.connect(host = '139.196.198.56', user='root' , passwd='Jth2016', db = 'zmap_empi', charset = 'utf8')
cur = conn.cursor()

query = "select * from zmap_r_patient where patient_name =" + "'" + name + "'"
cur.execute(query)
result = cur.fetchall()
print type(result)
# for i in range(result.__len__()):
#         print result[i][2],result[i][3],result[i][8]
#*******************************************************************************************************************


# for i in range(result.__len__()):
#         print result[i][0],result[i][1]
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
