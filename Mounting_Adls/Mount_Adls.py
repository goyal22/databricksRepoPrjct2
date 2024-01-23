# Databricks notebook source
# MAGIC %md
# MAGIC Mount the Bronze Layer Container:

# COMMAND ----------

dbutils.fs.mount(source = 'wasbs://bronzelayer@prjct2de.blob.core.windows.net', 
                 mount_point= '/mnt/bronzelayer', extra_configs ={'fs.azure.sas.bronzelayer.prjct2de.blob.core.windows.net':'?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2024-01-24T00:34:49Z&st=2024-01-23T16:34:49Z&spr=https&sig=DC5h6%2FcK8ooIasCpi2FqR2KDC5aVYN7%2FvQl17cuhYcQ%3D'})

# COMMAND ----------

# MAGIC %md 
# MAGIC Mount the Silver Layer Container:

# COMMAND ----------

dbutils.fs.mount(source = 'wasbs://silverlayer@prjct2de.blob.core.windows.net', 
                 mount_point= '/mnt/silverlayer', extra_configs ={'fs.azure.sas.silverlayer.prjct2de.blob.core.windows.net':'?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2024-01-24T00:34:49Z&st=2024-01-23T16:34:49Z&spr=https&sig=DC5h6%2FcK8ooIasCpi2FqR2KDC5aVYN7%2FvQl17cuhYcQ%3D'})

# COMMAND ----------

# MAGIC %md
# MAGIC Mount the Gold Layer Container

# COMMAND ----------

dbutils.fs.mount(source = 'wasbs://goldlayer@prjct2de.blob.core.windows.net', 
                 mount_point= '/mnt/goldlayer', extra_configs ={'fs.azure.sas.goldlayer.prjct2de.blob.core.windows.net':'?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2024-01-24T00:34:49Z&st=2024-01-23T16:34:49Z&spr=https&sig=DC5h6%2FcK8ooIasCpi2FqR2KDC5aVYN7%2FvQl17cuhYcQ%3D'})

# COMMAND ----------

# MAGIC %md 
# MAGIC Mount the processed Folder
# MAGIC

# COMMAND ----------

dbutils.fs.mount(source = 'wasbs://processed@prjct2de.blob.core.windows.net', 
                 mount_point= '/mnt/processed', extra_configs ={'fs.azure.sas.processed.prjct2de.blob.core.windows.net':'?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2024-01-24T00:34:49Z&st=2024-01-23T16:34:49Z&spr=https&sig=DC5h6%2FcK8ooIasCpi2FqR2KDC5aVYN7%2FvQl17cuhYcQ%3D'})

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls dbfs:/mnt/
