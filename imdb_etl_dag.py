from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.data_ingestion import ingest_data
from scripts.data_processing import process_data
from scripts.data_analysis import analyze_data


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 3, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "imdb_movie_pipeline",
    default_args=default_args,
    description="IMDb Movie Data Pipeline DAG",
    schedule_interval=timedelta(days=1),
)

ingest_task = PythonOperator(
    task_id="ingest_data",
    python_callable=ingest_data,
    dag=dag,
)

process_task = PythonOperator(
    task_id="process_data",
    python_callable=process_data,
    dag=dag,
)

analyze_task = PythonOperator(
    task_id="analyze_data",
    python_callable=analyze_data,
    dag=dag,
)

ingest_task >> process_task >> analyze_task