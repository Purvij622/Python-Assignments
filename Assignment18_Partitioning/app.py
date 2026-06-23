from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PartitionAssignment") \
    .getOrCreate()

# Generate 5 million records
df = spark.range(5000000)

print("\n===== INITIAL PARTITIONS =====")
print(df.rdd.getNumPartitions())

# Increase partitions to 12
df_repartition = df.repartition(12)

print("\n===== AFTER REPARTITION(12) =====")
print(df_repartition.rdd.getNumPartitions())

# Reduce partitions to 3
df_coalesce = df_repartition.coalesce(3)

print("\n===== AFTER COALESCE(3) =====")
print(df_coalesce.rdd.getNumPartitions())

spark.stop()