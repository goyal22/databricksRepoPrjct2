# Databricks notebook source
# MAGIC %sql
# MAGIC create database bronzeLayer

# COMMAND ----------

# MAGIC %sql
# MAGIC use database bronzeLayer

# COMMAND ----------

# MAGIC %sql
# MAGIC select current_database()%fs mounts

# COMMAND ----------

# MAGIC %fs mounts
