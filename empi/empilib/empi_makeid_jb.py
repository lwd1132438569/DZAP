#-*- coding: utf-8 -*-
#对每条记录产生empi_id
#找姓名重复值的SQL
#SELECT z.patient_name name , COUNT(z.patient_name) num FROM `zmap_r_patient` as z GROUP BY z.patient_name HAVING COUNT(z.patient_name) > 1 order by num desc;
#找姓名不重复的SQL
#SELECT z.patient_name name , COUNT(z.patient_name) num FROM `zmap_r_patient` as z GROUP BY z.patient_name HAVING COUNT(z.patient_name) = 1 order by num desc;

import pymysql
import jieba
import jieba.posseg
import jieba.analyse
import uuid
# s=set()
# def makeid():
#     while True:
#         a=str(uuid.uuid1())
#         b=a[:12]
#         if b not in s:
#             onlyid = b
#             s.add(b)
#             break
#
#     return onlyid
#**************************地址匹配模块暂时不用***********************************************
# def match(name,table_name):    #在具有多个姓名的记录中，
#     conn = pymysql.connect(host='139.196.198.56', user='root', passwd='Jth2016', db='zmap_empi', charset='utf8')
#     cur = conn.cursor()
#
#     query = "select * from " + table_name + "where patient_name =" + "'" + name + "'"
#     cur.execute(query)
#     result = cur.fetchall()  # result为tuple类型，记录存放是((),(),...()) 这样的形式
#     for i in range(result.__len__()):
#         if result[i][3] == '男':
#
#             query_man = "UPDATE " + table_name + "set empi_id=" + makeid() + "where patient_name =" + "'" + name + "'"
#             cur.execute(query_man)
#         else:
#             query_woman = "UPDATE " + table_name + "set empi_id=" + makeid()+ "where patient_name =" + "'" + name + "'"
#             cur.execute(query_woman)
#
#
# def addr_kw(addr):  # 命名的意思为addr_key words 即为地址关键词的获取。
#     res_list = []
#     for x in jieba.analyse.textrank(addr.strip(), 3):  # 记录很多地址都用空格进行了分割，去空格后可以增加分词的准确性。
#         res_list.append(x)
#     return res_list



# def initid():
conn = pymysql.connect(host='192.168.1.111', user='root', passwd='1234', db='zmap_empi', charset='utf8')
cur = conn.cursor()

# #情况1：对名字只出现一次的患者，他只有一条记录，那么就给其这一条记录一个empi_id
# sql_only1 = "SELECT z.patient_name name , COUNT(z.patient_name) num FROM zmap_r_patient_empi_jb as z GROUP BY z.patient_name HAVING COUNT(z.patient_name) = 1"
# cur.execute(sql_only1)      #这里，先找到名字不重复的所有字段
#
# result = cur.fetchall()
# only1_name_list = []        #列表存放名字不重复的患者记录的名字
# for i in range(result.__len__()):
#     name = result[i][0]
#     query = "UPDATE zmap_r_patient_empi_jb set empi_id=" + "'" + str(uuid.uuid1()) + "'" + "where patient_name =" + "'" + name + "'"
#     cur.execute(query)
#     conn.commit()

#情况2：对名字出现多次的患者
sql_more = "SELECT z.patient_name name , COUNT(z.patient_name) num FROM zmap_r_patient_empi_jb as z GROUP BY z.patient_name HAVING COUNT(z.patient_name) > 1"
cur.execute(sql_more)        #这里，先找到名字重复的所有字段
# conn.commit()
result_m = cur.fetchall()
more_name_list = []          #列表存放名字重复的患者记录的名字
for j in range(result_m.__len__()):
    more_name_list.append(result_m[j][0])

birthday_list = []           #存放生日
for j in range(more_name_list.__len__()):
    name = more_name_list[j]
    query_birthday = "SELECT r.patient_name,r.birthday,count(r.birthday) num from (SELECT * FROM zmap_r_patient_empi_jb where patient_name = " + "'" + name + "'" +") as r GROUP BY r.birthday"
    cur.execute(query_birthday)
    result_bir = cur.fetchall()

    for k in range(result_bir.__len__()):
        query_b_and_n = "UPDATE zmap_r_patient_empi_jb set empi_id=" + "'" + str(uuid.uuid1()) + "'" + "where patient_name =" + "'" + name + "'" + "and birthday =" + "'" + result_bir[k][1] + "'"
        cur.execute(query_b_and_n)
        conn.commit()
