import airflow
from airflow.models.dag import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator

from airflow.contrib.operators.ssh_operator import SSHOperator
from datetime import timedelta,datetime
from datetime import date


today = date.today()
d4 = today.strftime("%Y-%b-%d")

default_args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(1),
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(seconds=15),
    }



ssh_conn_id="index_conn_id"

with DAG('TestConnection',default_args=default_args,schedule_interval='55 1 * * *') as dag:

    start=DummyOperator(task_id="Start")

    t1 = SSHOperator(ssh_conn_id=ssh_conn_id,
                                task_id='ConnectionDAG',
                                command='python /home/indxportal/test.py',
                                dag=dag)

    end=DummyOperator(task_id="End")

start>>t1>>end
