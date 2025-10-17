from airflow import DAG
from airflow.operators import ShortCircuitOperator, EmptyOperator

# Use the ShortCircuitOperator to control whether a pipeline
# continues if a condition is satisfied or a truthy value is obtained.

cond_true = ShortCircuitOperator(
    task_id="condition_is_True",
    python_callable=lambda: True,
)

cond_false = ShortCircuitOperator(
    task_id="condition_is_False",
    python_callable=lambda: False,
)

ds_true = [EmptyOperator(task_id=f"true_{i}") for i in [1, 2]]
ds_false = [EmptyOperator(task_id=f"false_{i}") for i in [1, 2]]

chain(cond_true, *ds_true)
chain(cond_false, *ds_false)

# using @task decorator
@task.short_circuit()
def check_condition(condition):
    return condition

ds_true = [EmptyOperator(task_id=f"true_{i}") for i in [1, 2]]
ds_false = [EmptyOperator(task_id=f"false_{i}") for i in [1, 2]]

condition_is_true = check_condition.override(task_id="condition_is_true")(condition=True)
condition_is_false = check_condition.override(task_id="condition_is_false")(condition=False)

chain(condition_is_true, *ds_true)
chain(condition_is_false, *ds_false)