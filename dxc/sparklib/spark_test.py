"""SimpleApp"""

from pyspark import SparkContext

# logFile = "D:\spark-2.0.2-bin-hadoop2.7\README.md"
logFile = "/Users/lwd/dev/spark-2.0.2-bin-hadoop2.7/README.md"
sc = SparkContext("local","Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i"%(numAs, numBs))