#-*- coding: utf-8 -*-

#找重复值的SQL
#SELECT z.patient_name name , COUNT(z.patient_name) num FROM `zmap_r_patient` as z GROUP BY z.patient_name HAVING COUNT(z.patient_name) > 1 order by num desc;

import pandas as pd
import matplotlib.pyplot as plt
import pymysql
import jieba
import jieba.posseg
import jieba.analyse
import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
# import pymysql
#
# name = '下建芳'
# conn = pymysql.connect(host = '139.196.198.56', user='root' , passwd='Jth2016', db = 'zmap_empi', charset = 'utf8')
# cur = conn.cursor()
#
# query = "select * from zmap_r_patient where patient_name =" + "'" + name + "'"
# cur.execute(query)
# result = cur.fetchall()
# print result[0]
# for i in range(result.__len__()):
#         print result[i][2],result[i][3],result[i][8]
#*******************************************************************************************************************


#**********************测试empi_match模块的效果**********************************************************************
name = '下建芳'
sex = '女'
addr = '日照中心'

def addr_kw(addr):  # 命名的意思为addr_key words 即为地址关键词的提取。
    res_list = []
    for x in jieba.analyse.textrank(addr.strip(),3):  # 记录很多地址都用空格进行了分割，去空格后可以增加分词的准确性。
        res_list.append(x)
    return res_list

conn = pymysql.connect(host='139.196.198.56', user='root', passwd='Jth2016', db='zmap_empi', charset='utf8')
cur = conn.cursor()

query = "select * from zmap_r_patient where patient_name =" + "'" + name + "'" + "and sex =" + "'" + sex + "'"
cur.execute(query)
result = cur.fetchall()   #result为tuple类型，记录存放是((),(),...()) 这样的形式
res = list(result)
res_addr_empty = []       #存放地址为空的记录
res_final = []            #存放满足条件的所有记录，即最终结果
for i in range(res.__len__()):   #对于地址为空的患者记录，在列表中删除
    if res[i][8] == ' ':
        res_addr_empty.append(res[i])     #地址为空的单独加到一个列表res_addr_empty
        res.remove(res[i])                #这样res中保存的仅仅为地址不空的记录

addr_input = addr_kw(addr)

for j in range(res.__len__()):
    if set(addr_input).issubset(addr_kw(res[j][8])):
        res_final.append(res[j])

print res_final
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
