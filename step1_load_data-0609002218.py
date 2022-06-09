from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "step1_load_data-0609002218",
}

dag = DAG(
    "step1_load_data-0609002218",
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


# Operator source: examples/pipelines/run-generic-pipelines-on-apache-airflow/load_data.ipynb

op_f137d7f1_1109_4571_babe_b9c6a5ece042 = KubernetesPodOperator(
    name="load_data_1",
    namespace="default",
    image="amancevice/pandas:1.4.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.8.1/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.8.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.8.1/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.8.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'step1_load_data' --cos-endpoint http://mlops-0603.mshome.net:7003/ --cos-bucket airflow-task-artifacts --cos-directory 'step1_load_data-0609002218' --cos-dependencies-archive 'load_data-f137d7f1-1109-4571-babe-b9c6a5ece042.tar.gz' --file 'examples/pipelines/run-generic-pipelines-on-apache-airflow/load_data.ipynb' "
    ],
    task_id="load_data_1",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "step1_load_data-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)
