# Databricks notebook source
from pyspark.sql.functions import lit
schema="claim_id int, policy_id int, date_of_claim timestamp, claim_amount double, claim_status string, LastUpdatedTimeStamp timestamp"
df = spark.read.parquet("/mnt/landing/claimData/*.parquet",inferSchema=False,schema=schema)
df_withCol = df.withColumn("merge_flag",lit(False))
df_withCol.write.option("path","/mnt/bronzelayer/Claim").mode("append").saveAsTable("bronzelayer.Claim")

# COMMAND ----------

from datetime import datetime

def getFilePathWithDates(filePath):
    # get the current time in mm-dd-yyyy format
    current_time = datetime.now().strftime('%m-%d-%Y')
    new_file_path = filePath+'/'+current_time
    return new_file_path

# COMMAND ----------

dbutils.fs.mv("/mnt/landing/claimData", getFilePathWithDates("/mnt/processed/ClaimData"), True )
