# Databricks notebook source
from pyspark.sql.functions import lit
schema = "agent_id integer, agent_name string, agent_email string,agent_phone string, branch_id integer, create_timestamp timestamp"
df = spark.read.parquet("/mnt/landing/AgentData/*.parquet")
df.show()
df_with_flag = df.withColumn("merge_flag", lit(False))
df_with_flag.write.option("path", "/mnt/bronzelayer/Agent").mode("append").saveAsTable("bronzelayer.Agent")

# COMMAND ----------

# MAGIC %fs mounts

# COMMAND ----------

from datetime import datetime
def getFilePathWithDates(filePath):
    # get the current time in mm-dd-yyyy format
    current_time = datetime.now().strftime('%m-%d-%Y')
    new_file_path = filePath+'/'+current_time
    return new_file_path
dbutils.fs.mv("/mnt/landing/AgentData/", getFilePathWithDates('/mnt/processed/AgentData'), True)
