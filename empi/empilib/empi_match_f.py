#-*- coding: utf-8 -*-
import pymysql
import jieba
import jieba.posseg
import jieba.analyse
import uuid
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


def match(name, sex, birthday, addr):
        conn = pymysql.connect(host='192.168.1.111', user='root', passwd='1234', db='zmap_empi', charset='utf8')
        cur = conn.cursor()

        query = "select * from zmap_r_patient_empi_jb where patient_name =" + "'" + name + "'" + "and sex =" + "'" + sex + "'" + "and birthday like" + "'" + birthday + "%" + "'"
        cur.execute(query)
        result = cur.fetchall()  # result为tuple类型，记录存放是((),(),...()) 这样的形式
        res = list(result)
        res_addr_empty = []  # 存放地址为空的记录
        res_final = []  # 存放满足条件的所有记录，即最终结果
        for i in range(res.__len__()):  # 对于地址为空的患者记录，在列表中删除,res[j][5]
                if res[i][8] == ' ':
                        res_addr_empty.append(res[i])  # 地址为空的单独加到一个列表res_addr_empty
                        res.remove(res[i])  # 这样res中保存的仅仅为地址不空的记录

        addr_input = addr_kw(addr)

        for j in range(res.__len__()):
                if set(addr_input).issubset(addr_kw(res[j][8])):
                        res[j] = [res[j][1], res[j][2], res[j][3], res[j][4], res[j][5], res[j][6], res[j][7],
                                  res[j][8], res[j][10], res[j][19], res[j][21], res[j][32], res[j][42]]
                        # res[j]=[res[j][0],res[j][1],res[j][2],res[j][3],res[j][5],res[j][11],res[j][14],res[j][18],res[j][19],res[j][21],res[j][32]]
                        if res[j] not in res_final:
                                res_final.append(res[j])

        for k in range(res_final.__len__()):
                query_insert = "update zmap_r_patient_empi_jb set empi_id =" + "'" + str(
                        uuid.uuid1()) + "'" + "where patient_name =" + "'" + str(
                        res_final[k][1]) + "'" + "and sex =" + "'" + str(
                        res_final[k][2]) + "'" + "and addr =" + "'" + str(res_final[k][7]) + "'"
                cur.execute(query_insert)
                conn.commit()
        # res_final=str(res_final).replace('u\'', '\'')
        # res_final=res_final.decode("unicode-escape")


        return res_final
        # for i in range(result.__len__()):
        #         return result[i][2], result[i][3], result[i][8]

def match_id(name, sex, birthday, id_card, addr):
        conn = pymysql.connect(host='192.168.1.111', user='root', passwd='1234', db='zmap_empi', charset='utf8')
        cur = conn.cursor()

        query = "select * from zmap_r_patient_empi_jb where patient_name =" + "'" + name + "'" + "and sex =" + "'" + sex + "'" + "and birthday like" + "'" + birthday + "%" + "'" + "and id_card like" + "'" + id_card + "%" + "'"
        cur.execute(query)
        result = cur.fetchall()   #result为tuple类型，记录存放是((),(),...()) 这样的形式
        res = list(result)
        res_addr_empty = []       #存放地址为空的记录
        res_final = []            #存放满足条件的所有记录，即最终结果
        for i in range(res.__len__()):   #对于地址为空的患者记录，在列表中删除,res[j][5]
                if res[i][8] == ' ':
                        res_addr_empty.append(res[i])     #地址为空的单独加到一个列表res_addr_empty
                        res.remove(res[i])                #这样res中保存的仅仅为地址不空的记录

        addr_input = addr_kw(addr)

        for j in range(res.__len__()):
                if set(addr_input).issubset(addr_kw(res[j][8])):
                        res[j]=[res[j][1],res[j][2],res[j][3],res[j][4],res[j][5],res[j][6],res[j][7],res[j][8],res[j][10],res[j][19],res[j][21],res[j][32],res[j][42]]
                        #res[j]=[res[j][0],res[j][1],res[j][2],res[j][3],res[j][5],res[j][11],res[j][14],res[j][18],res[j][19],res[j][21],res[j][32]]
                        if res[j] not in res_final:
                                res_final.append(res[j])

        for k in range(res_final.__len__()):
            query_insert = "update zmap_r_patient_empi_jb set empi_id =" + "'" + str(uuid.uuid1()) + "'" + "where patient_name =" + "'" + str(res_final[k][1]) + "'" + "and sex =" + "'" + str(res_final[k][2]) + "'" + "and addr =" + "'" + str(res_final[k][7]) + "'"
            cur.execute(query_insert)
            conn.commit()
        # res_final=str(res_final).replace('u\'', '\'')
        # res_final=res_final.decode("unicode-escape")


        return res_final
        # for i in range(result.__len__()):
        #         return result[i][2], result[i][3], result[i][8]

def addr_kw(addr):     #命名的意思为addr_key words 即为地址关键词的提取。
        res_list = []
        for x in jieba.analyse.extract_tags(str(addr),3):    #记录很多地址都用空格进行了分割，去空格后可以增加分词的准确性。
                res_list.append(x)
        return res_list



