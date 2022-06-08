from airflow.operators.bash_operator import BashOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "exec_remote_command-0608032601",
}

dag = DAG(
    "exec_remote_command-0608032601",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.8.1 pipeline editor using `exec_remote_command.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "local-directory-catalog", "component_ref": {"base_dir": "/home/jovyan/work/examples/pipelines/run-pipelines-on-apache-airflow/components", "path": "http_operator.py"}}
op_f7a938d0_62ae_40dd_aee1_82716b2e3337 = SimpleHttpOperator(
    task_id="load_cmd",
    endpoint="https://api.github.com/repos/elyra-ai/examples/contents/pipelines/run-pipelines-on-apache-airflow/resources/command.txt",
    method="GET",
    data={"ref": "master"},
    headers={"Accept": "Accept:application/vnd.github.v3.raw"},
    response_check="",
    response_filter="",
    extra_options={},
    http_conn_id="http_github",
    log_response=False,
    dag=dag,
)


# Operator source: {"catalog_type": "local-directory-catalog", "component_ref": {"base_dir": "/home/jovyan/work/examples/pipelines/run-pipelines-on-apache-airflow/components", "path": "bash_operator.py"}}
op_b6676eb8_989d_402b_bf3a_707e946779af = BashOperator(
    task_id="exec_cmd",
    bash_command="{{ ti.xcom_pull(task_ids='load_cmd') }}",
    env={},
    output_encoding="utf-8",
    dag=dag,
)

op_b6676eb8_989d_402b_bf3a_707e946779af << op_f7a938d0_62ae_40dd_aee1_82716b2e3337
