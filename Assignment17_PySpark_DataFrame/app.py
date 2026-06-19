from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("SalesAnalysis") \
    .getOrCreate()

df = spark.read.csv(
    "sales.csv",
    header=True,
    inferSchema=True
)

print("\n===== SORTED PRODUCTS =====")

sorted_df = df.orderBy(col("sales").desc())
sorted_df.show()

print("\n===== TOP 3 PRODUCTS =====")

top3 = sorted_df.limit(3)
top3.show()

print("\n===== SALES > 80000 =====")

filtered_df = df.filter(col("sales") > 80000)
filtered_df.show()

filtered_df.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("filtered_products")

print("\nFiltered products saved successfully")

spark.stop()