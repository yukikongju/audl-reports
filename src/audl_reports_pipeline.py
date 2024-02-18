import textwrap
from datetime import datetime, timedelta

from airflow.models.dag import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from GameStatsExtraction import main as run_game_stats_extraction


default_args = {
    'owner': 'yukikongju',
    'depends_on_past': False,
    'start_date': datetime(2023,2,1),
    #  'end_date': datetime(2023, 2, 5),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}
dag = DAG('audl-reports', 
          default_args=default_args, 
          description='DAG for AUDL reports ELT pipeline', 
          schedule=timedelta(days=1))

# run GameStatsExtraction
t1 = PythonOperator(task_id='run_game_stats_extraction',
                    python_callable=run_game_stats_extraction,
                    # pass start_date and end_date as args
                    op_args=['{{ ds }}', '{{ tomorrow_ds }}'], 
                    dag=dag,
        )
t1

