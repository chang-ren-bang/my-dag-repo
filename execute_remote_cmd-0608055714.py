from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "execute_remote_cmd-0608055714",
}

dag = DAG(
    "execute_remote_cmd-0608055714",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.8.1 pipeline editor using `execute_remote_cmd.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "airflow-provider-package-catalog", "component_ref": {"provider_package": "apache_airflow_providers_http-2.1.2-py3-none-any.whl", "provider": "apache_airflow_providers_http", "file": "airflow/providers/http/operators/http.py"}}
op_59a60699_302a_422b_8c35_3efa267b7e76 = SimpleHttpOperator(
    task_id="load_cmd",
    endpoint="/repos/elyra-ai/examples/contents/pipelines/run-pipelines-on-apache-airflow/resources/command.txt",
    method="GET",
    data='{"ref": "master"}',
    headers={"Accept": "Accept:application/vnd.github.v3.raw"},
    response_check="",
    response_filter="",
    extra_options={},
    http_conn_id="http_github",
    log_response=False,
    auth_type="",
    dag=dag,
)


# Operator source: {"catalog_type": "airflow-package-catalog", "component_ref": {"airflow_package": "apache_airflow-2.3.2-py3-none-any.whl", "file": "airflow/operators/bash.py"}}
op_d3769a05_43dc_410c_bd18_3754575d4e76 = BashOperator(
    task_id="exec_cmd",
    bash_command="{{ ti.xcom_pull(task_ids='load_cmd') }}",
    env={"name": "World"},
    append_env=False,
    output_encoding="utf-8",
    skip_exit_code={"activeControl": "NumberControl", "NumberControl": 99},
    cwd="",
    dag=dag,
)

op_d3769a05_43dc_410c_bd18_3754575d4e76 << op_59a60699_302a_422b_8c35_3efa267b7e76
