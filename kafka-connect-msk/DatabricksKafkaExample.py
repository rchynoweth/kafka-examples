# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC <img src="https://i.pinimg.com/originals/e1/3f/67/e13f6703e4a52f2421ce4d5473604e40.png" width="400">
# MAGIC 
# MAGIC 
# MAGIC Note: We are using AWS MSK as a managed Kafka service.
# MAGIC 
# MAGIC Docs: https://docs.databricks.com/spark/latest/structured-streaming/kafka.html#apache-kafka

# COMMAND ----------

# DBTITLE 1,Set Secret Credentials
# You can connect to Kafka over either SSL/TLS encrypted connection, or with an unencrypted plaintext connection.
# In this case we will just do plain text. 
# You can use secrets to set this value if you would like. 
kafka_bootstrap_servers_plaintext = ""

# COMMAND ----------

# DBTITLE 1,Create your a Kafka topic unique to your name
# Full username, e.g. "ryan.chynoweth@databricks.com"
username = dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().apply('user')

# Short form of username, suitable for use as part of a topic name.
user = username.split("@")[0].replace(".","_")

# DBFS directory for this project, we will store the Kafka checkpoint in there
project_dir = f"/Users/{username}/kafka/streaming_json_demo"

checkpoint_location = f"{project_dir}/kafka_checkpoint"

topic = f"{user}_kafka_test" # ryan_chynoweth_kafka_test

# COMMAND ----------

print( username )
print( user )
print( project_dir )
print( checkpoint_location )
print( topic )

# COMMAND ----------

# DBTITLE 1,Streaming dataset
# MAGIC %fs ls /databricks-datasets/structured-streaming/events

# COMMAND ----------

# DBTITLE 1,Create UDF for UUID
from datetime import datetime
from pyspark.sql.functions import *
from pyspark.sql.types import *
from datetime import datetime
import random, string, uuid

uuidUdf= udf(lambda : uuid.uuid4().hex,StringType())

# COMMAND ----------

# DBTITLE 1,Loading streaming dataset
input_path = "/databricks-datasets/structured-streaming/events"
input_schema = spark.read.json(input_path).schema

input_stream = (spark
  .readStream
  .schema(input_schema)
  .option("maxFilesPerTrigger", 1)
  .json(input_path)
  .withColumn("processingTime", lit(datetime.now().timestamp()).cast("timestamp"))
  .withColumn("eventId", uuidUdf()))


# COMMAND ----------

# DBTITLE 1,WriteStream to Kafka
# Clear checkpoint location
dbutils.fs.rm(checkpoint_location, True)


(input_stream
   .select(col("eventId").alias("key"), to_json(struct(col('action'), col('time'), col('processingTime'))).alias("value"))
   .writeStream
   .trigger(processingTime='10 seconds') ## slows the streaming for demo purposes 
   .format("kafka")
   .option("kafka.bootstrap.servers", kafka_bootstrap_servers_plaintext )
   .option("kafka.security.protocol", "PLAINTEXT")
   .option("checkpointLocation", checkpoint_location )
   .option("topic", topic)
   .start()
)

# COMMAND ----------

# DBTITLE 1,ReadStream to Kafka
startingOffsets = "earliest"


kafka = (spark.readStream
  .format("kafka")
  .option("maxBytesPerTrigger", 200000)
  .option("kafka.bootstrap.servers", kafka_bootstrap_servers_plaintext ) 
  .option("subscribe", topic )
  .option("startingOffsets", startingOffsets )
  .load())

read_stream = kafka.select(col("key").cast("string").alias("eventId"), from_json(col("value").cast("string"), json_schema).alias("json"))

display(read_stream)

# COMMAND ----------

display(read_stream.select("eventId", "json.action", "json.time"))
