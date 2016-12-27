#-*- coding: utf-8 -*-
import pymysql

def match(name):
        conn = pymysql.connect(host='139.196.198.56', user='root', passwd='Jth2016', db='zmap_empi', charset='utf8')
        cur = conn.cursor()

        query = "select * from zmap_r_patient where patient_name =" + "'" + name + "'"
        cur.execute(query)
        result = cur.fetchall()
        res = []
        for i in range(result.__len__()):
                res.append(result[i][5])

        return res
        # for i in range(result.__len__()):
        #         return result[i][2], result[i][3], result[i][8]

