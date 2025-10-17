from airflow import DAG
from airflow.operators import TriggerDagRunOperator
from datetime import datetime,timedelta

default_args = {
    'owner': 'Kumar Govind',
    'depends_on_past': False,
    'retries': 1,
    'start_time': datetime(2023,1,1),
    'email_on_failure': False,
    'email_on_retry': False
}

with DAG(
    dag_id = 'trigger_dag_run_operator_dag',
    default_args=default_args,
    description = 'A simple DAG with TriggerDagRunOperator',
    schedule_interval=timedelta(days=1),
    catchup=False
) as dag:
    trigger1=TriggerDagRunOperator(
        task_id='trigger_bash_operator_dag',
        trigger_dag_id='bash_operator_dag'
    )
    trigger2=TriggerDagRunOperator(
        task_id ='trigger_python_operator_dag',
        trigger_dag_id='python_operator_dag'
    )

    trigger1 >> trigger2