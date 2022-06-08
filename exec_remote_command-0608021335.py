from airflow.operators.bash_operator import BashOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "exec_remote_command-0608021335",
}

dag = DAG(
    "exec_remote_command-0608021335",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.8.1 pipeline editor using `exec_remote_command.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "local-file-catalog", "component_ref": {"base_dir": "/home/jovyan/work/examples/pipelines/run-pipelines-on-apache-airflow/components", "path": "http_operator.py"}}
op_d341ee66_088c_4245_b1bd_70243335a654 = SimpleHttpOperator(
    task_id="load_command",
    endpoint="http://mlops-0603.mshome.net:7001/lab/tree/examples/pipelines/run-pipelines-on-apache-airflow/resources/command.txt",
    method="POST",
    data={},
    headers={},
    response_check="",
    extra_options={},
    xcom_push=True,
    http_conn_id="http_default",
    log_response=False,
    dag=dag,
)


# Operator source: {"catalog_type": "url-catalog", "component_ref": {"url": "https://raw.githubusercontent.com/elyra-ai/examples/main/pipelines/run-pipelines-on-apache-airflow/components/bash_operator.py"}}
op_4d6fb57c_e386_4fba_ae2c_da297de20ade = BashOperator(
    task_id="exec_command",
    bash_command="{{ ti.xcom_pull(task_ids='load_command') }}",
    xcom_push=False,
    env={"name": "Ben"},
    output_encoding="utf-8",
    dag=dag,
)

op_4d6fb57c_e386_4fba_ae2c_da297de20ade << op_d341ee66_088c_4245_b1bd_70243335a654
