# Databricks notebook source
CATALOG = "olist_lakehouse"
spark.sql(f"CREATE CATALOG IF NOT EXISTS {CATALOG}")
spark.sql(f"USE CATALOG {CATALOG}")

for s in ["bronze", "silver", "gold", "ops", "lab"]:
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{s}")

for v in ["seed", "landing", "checkpoints"]:
    spark.sql(f"CREATE VOLUME IF NOT EXISTS {CATALOG}.ops.{v}")

display(spark.sql(f"SHOW VOLUMES IN {CATALOG}.ops"))