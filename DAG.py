from this import d
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

with DAG(
    dag_id='process-data-prix-caburants',
    schedule_interval='5,35 4-20 * * *',
    start_date=days_ago(0, hour=1),
    dagrun_timeout=timedelta(minutes=15),
    tags=['carburants', 'prix'],
    params={},
) as dag:

    update_prix_carburants = BashOperator(
        task_id='update_prix_carburants',
        bash_command='/opt/airflow/dags/dag_process_data_dgv/update.sh ',
    )

    update_prix_carburants