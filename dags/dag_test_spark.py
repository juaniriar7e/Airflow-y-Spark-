from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "juan_pablo",
    "depends_on_past": False,
    "start_date": datetime(2026, 4, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "01_test_spark_connection",
    default_args=default_args,
    description="Prueba de SparkSubmitOperator hacia el cluster Bitnami",
    schedule_interval=None,  # Solo ejecución manual
    catchup=False,
    tags=["test", "pyspark"],
) as dag:
    test_spark_job = SparkSubmitOperator(
        task_id="run_pyspark_test",
        conn_id="spark_default",
        # IMPORTANTE: Esta ruta es DENTRO del contenedor de Spark
        application="/app/scripts/test_spark.py",
        name="airflow_test_job",
        verbose=True,
        conf={"spark.master": "spark://spark-master:7077"},
    )
