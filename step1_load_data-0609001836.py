from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "step1_load_data-0609001836",
}

dag = DAG(
    "step1_load_data-0609001836",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.8.1 pipeline editor using `step1_load_data.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "airflow-provider-package-catalog", "component_ref": {"provider_package": "apache_airflow_providers_papermill-2.2.3-py3-none-any.whl", "provider": "apache_airflow_providers_papermill", "file": "airflow/providers/papermill/operators/papermill.py"}}
op_5eca0662_6541_4980_b404_ff5a90b002f0 = PapermillOperator(
    task_id="load_data",
    input_nb="load_data.ipynb",
    output_nb="load_data_out.ipynb",
    parameters={},
    kernel_name="",
    dag=dag,
)
