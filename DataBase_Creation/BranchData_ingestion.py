# Databricks notebook source
from pyspark.sql.functions import lit
db_schema="branch_id int , branch_country string , branch_city string"
df= spark.read.parquet("/mnt/landing/BranchData/*.parquet",inferSchema=False,schema=db_schema)
df_merge = df.withColumn("merge_flag",lit(False))
df_merge.write.option("path","/mnt/bronzelayer/Branch").mode("append").saveAsTable("bronzelayer.Branch")

# COMMAND ----------

# MAGIC %fs mounts

# COMMAND ----------

from datetime import datetime

def getFilePathWithDates(filePath):
    # get the current time in mm-dd-yyyy format
    current_time = datetime.now().strftime('%m-%d-%Y')
    new_file_path = filePath+'/'+current_time
    return new_file_path

# COMMAND ----------

dbutils.fs.mv("/mnt/landing/BranchData/", getFilePathWithDates('/mnt/processed/BranchData'), True)
