#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import jieba
import jieba.posseg
import jieba.analyse

print('关键词提取')
print('-'*40)
print(' TF-IDF')
print('-'*40)

# f = open("../data/ndy.txt","r")
f = open("../data/nlp_test.txt","r")
s = f.read()

for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))

print('-'*40)
print(' TextRank')
print('-'*40)

for x in jieba.analyse.textrank(s,3):
    print('%s' % (x))