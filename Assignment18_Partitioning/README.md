# Assignment 18 - PySpark Partitioning

## Objective

Generate a DataFrame with 5 million records using spark.range().

### Operations

1. Display initial partitions
2. Increase partitions to 12 using repartition()
3. Reduce partitions to 3 using coalesce()

## Build

docker build -t partition-app .

## Run

docker run --rm partition-app