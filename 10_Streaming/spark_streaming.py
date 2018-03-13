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

#ssc = StreamingContext(sc, STREAMING_WINDOW)
#dstream = ssc.socketTextStream("localhost", 9999)

#lines = spark \
#    .readStream \
#    .format("socket") \
#    .option("host", "localhost") \
#    .option("port", 9999) \
#    .load()

#decayFactor=1.0
#timeUnit="batches"
#model = StreamingKMeans(k=10, decayFactor=decayFactor, timeUnit=timeUnit).setRandomCenters(3, 1.0, 0)

kmeans = KMeans(k=2, seed=1)

userSchema = StructType().add("x", "integer").add("y", "integer").add("z", "integer")

points = spark \
    .readStream \
    .schema(userSchema) \
    .csv(os.path.join(os.getcwd(), "data.csv")) 

# Split the lines into words
hasher = FeatureHasher(inputCols=["x", "y", "z"],
                       outputCol="features")

points_featurized = hasher.transform(points)
model = kmeans.fit(points_featurized)
#predictions = model.transform(points_featurized)

pipeline = Pipeline(stages=[hasher, model])
pipeline.fit(points)
                            

query = pipeline \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()

#all_points=points_featurized.select("features").rdd
#model.trainOn(all_points)
#model.predictOnValues(all_points)
#
#result.pprint()
#ssc.start()
#ssc.stop(stopSparkContext=True, stopGraceFully=True)

# Generate running word count
#wordCounts = words.groupBy("word").count()




#sc.start()
#ssc.awaitTermination()
#ssc.stop(stopSparkContext=True, stopGraceFully=True)


#decayFactor=1.0
#timeUnit="batches"
#model = StreamingKMeans(k=10, decayFactor=decayFactor, timeUnit=timeUnit).setRandomCenters(3, 1.0, 0)




#kafka_dstream = KafkaUtils.createStream(ssc, KAFKA_ZK, "spark-streaming-consumer", {TOPIC: 1})
#kafka_param: "metadata.broker.list": brokers
#kafka_dstream = KafkaUtils.createDirectStream(ssc, [TOPIC], {"metadata.broker.list": METABROKER_LIST })




#counts=[]
#kafka_dstream.foreachRDD(lambda t, rdd: counts.append(rdd.count()))
#global count_messages 
#count_messages  = sum(counts)
#
#output_file.write(str(counts))
#kafka_dstream.count().pprint()

#print str(counts)
#count = kafka_dstream.count().reduce(lambda a, b: a+b).foreachRDD(lambda a: a.count())
#if count==None:
#    count=0
#print "Number of Records: %d"%count


#points = kafka_dstream.transform(pre_process)
#points.pprint()
#points.foreachRDD(model_update)

#predictions=model_update(points)
#predictions.pprint()



#We create a model with random clusters and specify the number of clusters to find
#model = StreamingKMeans(k=10, decayFactor=1.0).setRandomCenters(3, 1.0, 0)
#points=kafka_dstream.map(lambda p: p[1]).flatMap(lambda a: eval(a)).map(lambda a: Vectors.dense(a))
#points.pprint()


# Now register the streams for training and testing and start the job,
# printing the predicted cluster assignments on new data points as they arrive.
#model.trainOn(trainingStream)
#result = model.predictOnValues(testingStream.map(lambda point: ))
#result.pprint()

# Word Count
#lines = kvs.map(lambda x: x[1])
#counts = lines.flatMap(lambda line: line.split(" ")) \
#        .map(lambda word: (word, 1)) \
#        .reduceByKey(lambda a, b: a+b)
#counts.pprint()

