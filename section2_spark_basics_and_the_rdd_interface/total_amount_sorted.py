from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("totalAmountSorted")
sc = SparkContext(conf = conf)

def extract_customer_price(line):
    fields = line.split(',')
    return (int(fields[0]), float(fields[2]))

lines = sc.textFile("./customer-orders.csv")
mapped_input = lines.map(extract_customer_price)
total_by_customer = mapped_input.reduceByKey(lambda x, y: x + y)

total_sorted = total_by_customer.sortBy(lambda x: x[1])

results = total_sorted.collect()
for result in results:
    print(result)