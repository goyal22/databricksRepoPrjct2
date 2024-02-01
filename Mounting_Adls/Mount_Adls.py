# Databricks notebook source
# MAGIC %md
# MAGIC Mount the Bronze Layer Container:

# COMMAND ----------

dbutils.fs.updateMount(source = 'wasbs://bronzelayer@prjct2de.blob.core.windows.net', 
                 mount_point= '/mnt/bronzelayer', extra_configs ={'fs.azure.sas.bronzelayer.prjct2de.blob.core.windows.net':'?sv=2022-11-02&ss=bfqt&srt=co&sp=rwdlacupyx&se=2024-02-29T17:31:07Z&st=2024-02-01T09:31:07Z&spr=https&sig=9G%2FJXX%2FQ9RfZDE%2FtimadoB4%2BLqn9N2fbh9pSN7gw3qA%3D'})

# COMMAND ----------

# MAGIC %md 
# MAGIC Mount the Silver Layer Container:

# COMMAND ----------

dbutils.fs.updateMount(source = 'wasbs://silverlayer@prjct2de.blob.core.windows.net', 
                 mount_point= '/mnt/silverlayer', extra_configs ={'fs.azure.sas.silverlayer.prjct2de.blob.core.windows.net':'?sv=2022-11-02&ss=bfqt&srt=co&sp=rwdlacupyx&se=2024-02-29T17:31:07Z&st=2024-02-01T09:31:07Z&spr=https&sig=9G%2FJXX%2FQ9RfZDE%2FtimadoB4%2BLqn9N2fbh9pSN7gw3qA%3D'})

# COMMAND ----------

# MAGIC %md
# MAGIC Mount the Gold Layer Container

# COMMAND ----------

dbutils.fs.updateMount(source = 'wasbs://goldlayer@prjct2de.blob.core.windows.net', 
                 mount_point= '/mnt/goldlayer', extra_configs ={'fs.azure.sas.goldlayer.prjct2de.blob.core.windows.net':'?sv=2022-11-02&ss=bfqt&srt=co&sp=rwdlacupyx&se=2024-02-29T17:31:07Z&st=2024-02-01T09:31:07Z&spr=https&sig=9G%2FJXX%2FQ9RfZDE%2FtimadoB4%2BLqn9N2fbh9pSN7gw3qA%3D'})

# COMMAND ----------

# MAGIC %md 
# MAGIC Mount the processed Folder
# MAGIC

# COMMAND ----------

dbutils.fs.updateMount(source = 'wasbs://processed@prjct2de.blob.core.windows.net', 
                 mount_point= '/mnt/processed', extra_configs ={'fs.azure.sas.processed.prjct2de.blob.core.windows.net':'?sv=2022-11-02&ss=bfqt&srt=co&sp=rwdlacupyx&se=2024-02-29T17:31:07Z&st=2024-02-01T09:31:07Z&spr=https&sig=9G%2FJXX%2FQ9RfZDE%2FtimadoB4%2BLqn9N2fbh9pSN7gw3qA%3D'})

# COMMAND ----------

dbutils.fs.updateMount(source = 'wasbs://landing@prjct2de.blob.core.windows.net', 
                 mount_point= '/mnt/landing', extra_configs ={'fs.azure.sas.landing.prjct2de.blob.core.windows.net':'?sv=2022-11-02&ss=bfqt&srt=co&sp=rwdlacupyx&se=2024-02-29T17:31:07Z&st=2024-02-01T09:31:07Z&spr=https&sig=9G%2FJXX%2FQ9RfZDE%2FtimadoB4%2BLqn9N2fbh9pSN7gw3qA%3D'})

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls dbfs:/mnt/

# COMMAND ----------

# Get the list of mounted points
mounted_points = dbutils.fs.mounts()

# Print information about each mounted point
for mount_point in mounted_points:
    print(f"Mount Point: {mount_point.mountPoint}, Source: {mount_point.source}")
