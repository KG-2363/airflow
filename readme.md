--python version = 3.13.9 

--Created py venv 

. .\py_env\Scripts\Activate.ps1

& .\py_env\Scripts\Activate.ps1

--Installed Airflow
py_env\Scripts\python.exe --version and it returned Python 3.13.9, so use the constraints file for 3.13.

python -m pip install "apache-airflow==3.1.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.1.0/constraints-3.13.txt"

for not on venev -- 

& "C:\Users\KumarGovind\Desktop\My Learnings\Github\airflow\py_env\Scripts\python.exe" -m pip install "apache-airflow==3.1.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.1.0/constraints-3.13.txt"

--verify installation 
python -m pip show apache-airflow
python -c 'import airflow; print(airflow.__version__)'

-- AIRFLOW HOME 
$env:AIRFLOW_HOME = (Get-Location).Path
VERIFY -echo $env:AIRFLOW_HOME

-- initialize airflow db 
airflow db init -- command outdated in 2... versions now -- 
airflow db migrate

--
mkdir dags logs plugins
``
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.1/docker-compose.yaml'

echo AIRFLOW_UID=50000 > .env

echo AIRFLOW_UID=50000 | Out-File -Encoding ASCII .env

docker compose up airflow-init

docker compose up

http://localhost:8080



