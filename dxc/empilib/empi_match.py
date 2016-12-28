#-*- coding: utf-8 -*-
import pymysql
import jieba
import jieba.posseg
import jieba.analyse

def match(name,sex):
        conn = pymysql.connect(host='139.196.198.56', user='root', passwd='Jth2016', db='zmap_empi', charset='utf8')
        cur = conn.cursor()

        query = "select * from zmap_r_patient where patient_name =" + "'" + name + "'" + "and sex =" + "'" + sex + "'"
        cur.execute(query)
        result = cur.fetchall()   #result为tuple类型，记录存放是((),(),...()) 这样的形式
        res = list(result)
        for i in range(res.__len__()):   #对于地址为空的患者记录，在列表中删除
                if res[i][8] == ' ':
                        res.remove(res[i])

        addr_list = []     #存放满足条件的每条记录的地址
        for i in range(result.__len__()):
                addr_list.append(result[i][8])

        return res
        # for i in range(result.__len__()):
        #         return result[i][2], result[i][3], result[i][8]

def addr_kw(addr):     #命名的意思为addr_key words 即为地址关键词的提取。
        res_list = []
        for x in jieba.analyse.textrank(addr.strip(),2):    #记录很多地址都用空格进行了分割，去空格后可以增加分词的准确性。
                res_list.append(x)
        return res_list



