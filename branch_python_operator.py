from airflow import DAG
from airflow.operators import BranchPythonOperator


# Note: Passing a caching dir allows to keep the virtual environment 
#       over multiple runs
# Run the example a second time and see that it reuses it and is faster.

VENV_CACHE_PATH = Path(tempfile.gettempdir())

def branch_with_venv(choices):
    import random

    import numpy as np

    print(f"Some numpy stuff: {np.arange(6)}")
    return f"venv_{random.choice(choices)}"

branching_venv = BranchPythonVirtualenvOperator(
    task_id="branching_venv",
    requirements=["numpy~=1.26.0"],
    venv_cache_path=VENV_CACHE_PATH,
    python_callable=branch_with_venv,
    op_args=[options],
)

# using @task decorator
@task.branch_virtualenv(requirements=["numpy~=1.26.0"], venv_cache_path=VENV_CACHE_PATH)
def branching_virtualenv(choices) -> str:
    import random

    import numpy as np

    print(f"Some numpy stuff: {np.arange(6)}")
    return f"venv_{random.choice(choices)}"