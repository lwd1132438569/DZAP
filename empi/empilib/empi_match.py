#-*- coding: utf-8 -*-
import pymysql
import jieba
import jieba.posseg
import jieba.analyse

def match(name,sex,addr):
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

        return res_final
        # for i in range(result.__len__()):
        #         return result[i][2], result[i][3], result[i][8]

def addr_kw(addr):     #命名的意思为addr_key words 即为地址关键词的提取。
        res_list = []
        for x in jieba.analyse.textrank(addr.strip(),3):    #记录很多地址都用空格进行了分割，去空格后可以增加分词的准确性。
                res_list.append(x)
        return res_list



