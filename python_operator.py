from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime, timedelta

def pre_process():
    print("Pre-processing data...")

def process_data():
    print("Processing data...")

def post_process():
    print("Post-processing data...")

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
    dag_id='python_operator_dag',
    default_args=default_args,
    description='A simple DAG with PythonOperator',
    schedule_interval=timedelta(days=1),
    catchup=False 
) as dag:
    
    pre_process_task = PythonOperator(
        task_id='pre_process',
        python_callable=pre_process
    )

    process_data_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data
    )

    post_process_task = PythonOperator(
        task_id='post_process',
        python_callable=post_process
    )

    pre_process_task >> process_data_task >> post_process_task
    