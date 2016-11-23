from pyspark.ml.linalg import Vectors
from pyspark.ml.regression import LinearRegression
from pyspark import SparkContext
from pyspark import SQLContext

sc = SparkContext("local","Simple App")
sqlContext = SQLContext(sc)
df = sqlContext.createDataFrame([
     (1.0, 2.0, Vectors.dense(1.0)),
     (0.0, 2.0, Vectors.sparse(1, [], []))], ["label", "weight", "features"])

lr = LinearRegression(maxIter=5, regParam=0.0, solver="normal", weightCol="weight")
model = lr.fit(df)
test0 = sqlContext.createDataFrame([(Vectors.dense(-1.0),)], ["features"])

print abs(model.transform(test0).head().prediction - (-1.0)) < 0.001