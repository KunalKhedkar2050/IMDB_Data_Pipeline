🎬 IMDb Movie Data Pipeline

📌 Overview

The IMDb Movie Data Pipeline is an end-to-end data engineering project that extracts, processes, and analyzes IMDb movie data using Apache Airflow, AWS S3, and PySpark. The pipeline automates data ingestion, transformation, and analysis to generate valuable movie insights.

🚀 Tech Stack

Apache Airflow 🌀 - Orchestrates the data pipeline.

AWS S3 ☁️ - Stores raw and processed data.

PySpark 🔥 - Handles large-scale data processing.

Delta Lake 📊 - Efficient storage for transformed data.

Pandas 🐼 - Used for initial data ingestion.

Boto3 🛠 - Manages AWS S3 interactions.

🔄 Pipeline Workflow

Data Ingestion 📥 - Extracts IMDb movie dataset and uploads it to AWS S3.

Data Processing 🛠 - Cleans, transforms, and stores data using PySpark and Delta Lake.

Data Analysis 📊 - Queries transformed data for movie insights.

Orchestration ⏳ - Uses Apache Airflow to automate and schedule the pipeline.
