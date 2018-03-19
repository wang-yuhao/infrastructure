#!/bin/python
#
# with Kafka
#/naslx/projects/ug201/di57hah/students/software/spark-2.3.0-bin-hadoop2.7/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0 spark_streaming.py 
#
# without Kafka
#/naslx/projects/ug201/di57hah/students/software/spark-2.3.0-bin-hadoop2.7/bin/spark-submit spark_streaming.py 



import os
import sys
import time
import datetime
import logging
import numpy as np
import socket
import re
from subprocess import check_output

from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.clustering import StreamingKMeans
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.types import StructType
from pyspark.ml.feature import FeatureHasher
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml import Pipeline
from pyspark.sql import functions as F

#######################################################################################
# CONFIGURATIONS
# Get current cluster setup from work directory
#KAFKA_ZK=
#METABROKER_LIST=",".join(kafka_details[0])
TOPIC='KmeansList'
STREAMING_WINDOW=60

# Initialize PySpark
SPARK_MASTER="local[1]"
#SPARK_MASTER="spark://mpp3r03c04s06.cos.lrz.de:7077"
APP_NAME = "PySpark Lecture"
os.environ["PYSPARK_PYTHON"] = "/naslx/projects/ug201/di57hah/anaconda2/envs/python3/bin/python"

# If there is no SparkSession, create the environment
try:
    sc and spark
except NameError as e:
    import pyspark
    import pyspark.sql
    conf=pyspark.SparkConf().set("spark.cores.max", "4")
    sc = pyspark.SparkContext(master=SPARK_MASTER, conf=conf)
    spark = pyspark.sql.SparkSession(sc).builder.appName(APP_NAME).getOrCreate()

print("PySpark initiated...") 

lines = spark \
        .readStream \
        .text(os.path.join(os.getcwd(), "../data/nasa/spark-streaming/"))     
  

# https://stackoverflow.com/questions/40467936/how-do-i-get-the-last-item-from-a-list-using-pyspark

lines = lines.withColumn('split_value', F.split((lines.value), " "))
lines = lines.withColumn('response_code', lines.split_value[F.size(lines.split_value)-2])
rc_counts = lines.groupBy("response_code").count()
    

#append:Only the new rows in the streaming DataFrame/Dataset will be written to the sink
#complete:All the rows in the streaming DataFrame/Dataset will be written to the sink every time these is some updates
#update:only the rows that were updated in the streaming DataFrame/Dataset will be written to the sink every time there are some updates. If the query doesn’t contain aggregations, it will be equivalent to append mode.

query = rc_counts \
    .writeStream \
    .outputMode("update") \
    .format("console") \
    .trigger(processingTime='5 seconds')\
    .start()

query.awaitTermination()

