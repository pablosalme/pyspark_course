from pyspark.sql import SparkSession
from pyspark.sql import functions as func

spark = SparkSession.builder.appName("SparksSQL").getOrCreate()

people = spark.read.option("header", "true").option("inferSchema", "true").csv("./fakefriends-header.csv")

people_filtered = people.select(people.age, people.friends)
people_filtered.groupBy("age").avg("friends").sort("age").show()

#good formating
people_filtered.groupBy("age").agg(func.round(func.avg("friends"), 2)).sort("age").show()

#with custom column name
people_filtered.groupBy("age").agg(func.round(func.avg("friends"), 2).alias("friends_avg")).sort("age").show()

spark.stop()