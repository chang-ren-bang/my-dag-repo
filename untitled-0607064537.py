from airflow.operators.bash_operator import BashOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "untitled-0607064537",
}

dag = DAG(
    "untitled-0607064537",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.8.1 pipeline editor using `untitled.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "local-file-catalog", "component_ref": {"base_dir": "/home/jovyan/work/examples/pipelines/run-pipelines-on-apache-airflow/components", "path": "http_operator.py"}}
op_1c85dc91_db50_4a06_90f2_08758a2b60e1 = SimpleHttpOperator(
    task_id="HTTP_Request_1",
    endpoint="/repos/elyra-ai/examples/contents/pipelines/run-pipelines-on-apache-airflow/resources/command.txt",
    method="GET",
    data={"ref": "master"},
    headers={"Accept": "Accept:application/vnd.github.v3.raw"},
    response_check="",
    extra_options={},
    xcom_push=True,
    http_conn_id="http_github",
    log_response=False,
    dag=dag,
)


# Operator source: {"catalog_type": "url-catalog", "component_ref": {"url": "https://raw.githubusercontent.com/elyra-ai/examples/main/pipelines/run-pipelines-on-apache-airflow/components/bash_operator.py"}}
op_ce8a60ec_a517_46af_a98c_7f1a7ed7a0f6 = BashOperator(
    task_id="BashOperator",
    bash_command="{{ ti.xcom_pull(task_ids='HTTP_Request_1') }}",
    xcom_push=False,
    env={"name": "World"},
    output_encoding="utf-8",
    dag=dag,
)

op_ce8a60ec_a517_46af_a98c_7f1a7ed7a0f6 << op_1c85dc91_db50_4a06_90f2_08758a2b60e1
