from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct, avg, expr
from config.aws_config import AWS_S3_RAW_BUCKET, AWS_S3_PROCESSED_BUCKET

def process_data():
    spark = SparkSession.builder.appName("IMDbProcessing").getOrCreate()
    df = spark.read.csv(f"s3://{AWS_S3_RAW_BUCKET}/imdb_raw.csv", header=True, inferSchema=True)
    
    df_clean = df.dropna().filter(col("titleType") == "movie")
    df_clean = df_clean.withColumn("startYear", col("startYear").cast("int"))
    
    # Add a new column for decade classification
    df_clean = df_clean.withColumn("Decade", expr("floor(startYear/10) * 10"))
    
    # Compute average runtime per genre
    df_runtime = df_clean.groupBy("genres").agg(avg("runtimeMinutes").alias("Avg_Runtime"))
    df_runtime.write.format("delta").mode("overwrite").save(f"s3://{AWS_S3_PROCESSED_BUCKET}/imdb_runtime.delta")
    
    df_clean.write.format("delta").mode("overwrite").save(f"s3://{AWS_S3_PROCESSED_BUCKET}/imdb_processed.delta")
  
