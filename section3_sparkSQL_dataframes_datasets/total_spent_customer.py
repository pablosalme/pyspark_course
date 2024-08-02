from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType

spark = SparkSession.builder.appName("TotalSpentCustomer").getOrCreate()

schema = StructType([StructField("customerID", IntegerType(), True), StructField("itemID", IntegerType(), True), StructField("amountSpent", FloatType(), True)])

df = spark.read.schema(schema).csv("./customer-orders.csv")
df.printSchema()

total_group = df.groupBy("customerID").sum("amountSpent")
total_group_rounded = total_group.withColumn("amountSpent", func.round(func.col("sum(amountSpent)"), 2)).select("customerID", "amountSpent").sort("amountSpent")

total_group_rounded.show(total_group_rounded.count())

spark.stop()