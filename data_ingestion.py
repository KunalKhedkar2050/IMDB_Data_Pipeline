import boto3
import pandas as pd
from config.aws_config import AWS_S3_RAW_BUCKET, AWS_REGION

def ingest_data():
    imdb_url = "https://datasets.imdbws.com/title.basics.tsv.gz"
    df = pd.read_csv(imdb_url, sep="\t", low_memory=False)
    df.to_csv("/tmp/imdb_raw.csv", index=False)
    
    s3 = boto3.client("s3", region_name=AWS_REGION)
    s3.upload_file("/tmp/imdb_raw.csv", AWS_S3_RAW_BUCKET, "imdb_raw.csv")
    print("IMDb data uploaded to S3 successfully!")


 