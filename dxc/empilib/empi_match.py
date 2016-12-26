#-*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect(host = '139.196.198.56', user='root' , passwd='Jth2016', db = 'zmap_empi', charset = 'utf8')
cur = conn.cursor()

query = "SELECT * from " \
        "(SELECT z.patient_name name , COUNT(z.patient_name) the_sum FROM zmap_r_patient as z GROUP BY z.patient_name HAVING COUNT(z.patient_name) > 1 AND name != '') as a,zmap_r_patient b " \
        "where b.patient_name = a.name ORDER BY a.name"
cur.execute(query)
result = cur.fetchall()
for i in range(48,75):
        print result[i][0],result[i][1]

