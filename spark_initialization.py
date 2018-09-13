##############################################################################################
#   Name: spark_initialization.py                                                            #
#                                                                                            #
#   Description: This python script is used to initialize spark 1.6 and spark 2.1 creating   #
#                   spark context and spark session                                          #
#                                                                                            #
#   Parameters:                                                                              #
#   Authors: Priyesh Agrawal                                                                 #
#                                                                                            #
#                                                                                            #
#   Change Log:                                                                              #
#                                                                                            #
#       Date                Changed By              Description                              #
#   13-Sep-2018          Priyesh Agrawal        Initial creation                             #
##############################################################################################

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

spark= SparkSession.builder.master().appName().config.getOrCreate()

