# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC Fork https://github.com/Stano-D/cicd_basic_example_public 
# MAGIC
# MAGIC
# MAGIC 1 fork/copy/clone repo to your own repo
# MAGIC
# MAGIC 2 allow github action in repo
# MAGIC
# MAGIC 3 generate DATABRICKS_TOKEN and set secrets in repo (settings -> secrets and variables -> secrets)
# MAGIC
# MAGIC 4 set variable DATABRICKS_HOST (url of the databricks workspace)
# MAGIC
# MAGIC 5 clone repo to the databricks
# MAGIC
# MAGIC 6 create new branch in databricks repo
# MAGIC
# MAGIC 7 create new change
# MAGIC
# MAGIC 8 commit change
# MAGIC
# MAGIC 9 create pull request
# MAGIC
# MAGIC 10 merge to main branch in git repo
# MAGIC
# MAGIC Watch your triggered action in "action" (second from left in top panel in git)

# COMMAND ----------

print("This is just a test for commit on db.")
print("Second test.")

