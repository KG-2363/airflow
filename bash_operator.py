from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Kumar Govind',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,    
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
with DAG(
    dag_id='bash_operator_dag',
    default_args=default_args,
    description='A simple DAG with BashOperator',
    schedule_interval=timedelta(days=1),
    catchup=False 
) as dag:
    
    list_gcs_files = BashOperator(
        task_id='list_gcs_files',
        bash_command='gsutil ls gs://dataproc_jobs_bucket_kumar/*'
    )
    list_local_files = BashOperator(
        task_id='list_local_files',
        bash_command='ls -l /home/airflow/gcs/data/'
    )

    list_gcs_files >> list_local_files