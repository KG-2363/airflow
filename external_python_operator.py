from airflow import DAG
from airflow.operators import ExternalPythonOperator
from datetime import datetime, timedelta

"""
The ExternalPythonOperator can help you to run some of your tasks 
with a different set of Python libraries than other tasks 
(and than the main Airflow environment). 
This might be a virtual environment or any installation of Python
that is preinstalled and available in the environment where Airflow task is running.
The operator takes Python binary as python parameter. Note, that even

"""

def callable_external_python():
    """
    Example function that will be performed in a virtual environment.
    Importing at the module level ensures that it will not attempt to import the
    library before it is installed.
    """
    import sys
    from time import sleep

    print(f"Running task via {sys.executable}")
    print("Sleeping")
    for _ in range(4):
        print("Please wait...", flush=True)
        sleep(1)
    print("Finished")

external_python_task = ExternalPythonOperator(
    task_id="external_python",
    python_callable=callable_external_python,
    python=PATH_TO_PYTHON_BINARY,
)

# using @task decorator
@task.external_python(task_id="external_python", python=PATH_TO_PYTHON_BINARY)
def callable_external_python():
    """
    Example function that will be performed in a virtual environment.

    Importing at the module level ensures that it will not attempt to import the
    library before it is installed.
    """
    import sys
    from time import sleep

    print(f"Running task via {sys.executable}")
    print("Sleeping")
    for _ in range(4):
        print("Please wait...", flush=True)
        sleep(1)
    print("Finished")

external_python_task = callable_external_python()