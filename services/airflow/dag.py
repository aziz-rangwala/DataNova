from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "DataNova",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

with DAG("datanova_pipeline", default_args=default_args, start_date=datetime(2025, 1, 1), schedule_interval="0 * * * *") as dag:
    start_mock_data = DockerOperator(
        task_id="start_mock_data",
        image="mock-data",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge"
    )

    run_spark_etl = DockerOperator(
        task_id="run_spark_etl",
        image="spark-transformer",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge"
    )

    start_mock_data >> run_spark_etl

