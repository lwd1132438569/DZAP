from __future__ import print_function

from operator import add

from pyspark.sql import SparkSession
from pyspark import SparkContext

inputfile = '../data/test.txt'

# if __name__ == "__main__":
#     # sc = SparkContext("local", "Simple App")
#     # rdd = sc.textFile(inputfile).cache()
#     # num = rdd.count()
#     # print(num)    #97
#     spark = SparkSession\
#         .builder\
#         .appName("PythonWordCount")\
#         .getOrCreate()
#     lines = spark.read.text(inputfile).rdd.map(lambda r: r[0])
#     num = lines.count()
    # counts = lines.flatMap(lambda x: x.split(' ')) \
    #               .map(lambda x: (x, 1)) \
    #               .reduceByKey(add)
    # output = counts.collect()
    # for (word, count) in output:
    #     print("%s: %i" % (word, count))

    # spark.stop()

def wordcount(inputfile):
    spark = SparkSession \
        .builder \
        .appName("PythonWordCount") \
        .getOrCreate()
    lines = spark.read.text(inputfile).rdd.map(lambda r: r[0])
    num = lines.count()
    return  num
#     counts = lines.flatMap(lambda x: x.split(' ')) \
#         .map(lambda x: (x, 1)) \
#         .reduceByKey(add)
#     output = counts.count()
#     return output
#     # for (word, count) in output:
#     #     # print("%s: %i" % (word, count))
#     #     return [word,count]
#
#     # spark.stop()
