from airflow import DAG
from datetime import datetime
from custom_operator.my_custom_operator import CustomLivyOperator

with DAG(
    dag_id="Livy_Custom_Op",
    schedule_interval="@daily",
    start_date=datetime(2025, 4, 7, hour=14, minute=28),
    catchup=False,
) as dag:


    livy_job = CustomLivyOperator(
     task_id="livy_job",
     fabric_conn_id = "fabric",
     livy_conn_id='fabric_livy', # Livy Connection with api endpoint (not including /batches or /sessions) as host
     file='abfss://JJTest2@onelake.dfs.fabric.microsoft.com/lhJohn.Lakehouse/Files/code/spark-query-lh.py', # File in lakehouse to run
     polling_interval=60,
     dag=dag
    )
    
    livy_job
    