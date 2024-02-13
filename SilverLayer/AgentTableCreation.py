# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC create table Silverlayer.Agent
# MAGIC (
# MAGIC     agent_id integer, 
# MAGIC     agent_name string,
# MAGIC     agent_email string,
# MAGIC     agent_phone string,
# MAGIC     branch_id integer,
# MAGIC     create_timestamp timestamp
# MAGIC   )using DELTA LOCATION '/mnt/silverlayer/Agent'

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table Silverlayer.Agent
