from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, TimestampType

schema = StructType() \
    .add("user_id", StringType()) \
    .add("name", StringType()) \
    .add("email", StringType()) \
    .add("event_type", StringType()) \
    .add("timestamp", TimestampType()) \
    .add("metadata", StringType())

spark = SparkSession.builder \
    .appName("Kafka-Spark-Cassandra ETL") \
    .config("spark.cassandra.connection.host", "cassandra") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "events") \
    .load()

parsed_df = df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"), schema).alias("data")).select("data.*")
parsed_df.writeStream \
    .format("org.apache.spark.sql.cassandra") \
    .option("keyspace", "datanova") \
    .option("table", "events") \
    .start() \
    .awaitTermination()