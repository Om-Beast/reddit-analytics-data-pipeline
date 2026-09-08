import os
import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
)

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline
from utils.constants import POST_LIMIT, SUBREDDIT


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "data", "output")


default_args = {
    "owner": "reddit-analytics-pipeline",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="reddit_analytics_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["reddit", "etl", "aws", "data-engineering"],
    max_active_runs=1,
) as dag:

    file_name = (
        f"reddit_{datetime.now().strftime('%Y%m%d')}.csv"
    )

    file_path = os.path.join(
        OUTPUT_DIR,
        file_name,
    )

    object_key = (
        f"raw/reddit/"
        f"year={datetime.now().year}/"
        f"month={datetime.now().month:02d}/"
        f"day={datetime.now().day:02d}/"
        f"{file_name}"
    )

    extract_reddit = PythonOperator(
        task_id="extract_and_transform_reddit",
        python_callable=reddit_pipeline,
        op_kwargs={
            "file_path": file_path,
            "subreddit": SUBREDDIT,
            "time_filter": "day",
            "limit": POST_LIMIT,
        },
    )

    upload_to_s3 = PythonOperator(
        task_id="upload_to_s3",
        python_callable=upload_s3_pipeline,
        op_kwargs={
            "file_path": file_path,
            "object_key": object_key,
        },
    )

    extract_reddit >> upload_to_s3