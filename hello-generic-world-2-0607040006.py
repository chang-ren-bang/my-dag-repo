from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "hello-generic-world-2-0607040006",
}

dag = DAG(
    "hello-generic-world-2-0607040006",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.8.1 pipeline editor using `hello-generic-world-2.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "airflow-provider-package-catalog", "component_ref": {"provider_package": "apache_airflow_providers_papermill-2.2.3-py3-none-any.whl", "provider": "apache_airflow_providers_papermill", "file": "airflow/providers/papermill/operators/papermill.py"}}
op_dffdc7c8_5cd6_4f3d_8c32_f7579ea79079 = PapermillOperator(
    task_id="load_data_ipynb",
    input_nb="load_data.ipynb",
    output_nb="load_data_out.ipynb",
    parameters={},
    kernel_name="",
    dag=dag,
)


# Operator source: {"catalog_type": "airflow-provider-package-catalog", "component_ref": {"provider_package": "apache_airflow_providers_papermill-2.2.3-py3-none-any.whl", "provider": "apache_airflow_providers_papermill", "file": "airflow/providers/papermill/operators/papermill.py"}}
op_0a1b4861_a7b3_4b5c_a1be_8f2f0fb25d88 = PapermillOperator(
    task_id="Part_1___Data_Cleaning_ipynb",
    input_nb="Part 1 - Data Cleaning.ipynb",
    output_nb="Part 1 - Data Cleaning_out.ipynb",
    parameters={},
    kernel_name="",
    dag=dag,
)

op_0a1b4861_a7b3_4b5c_a1be_8f2f0fb25d88 << op_dffdc7c8_5cd6_4f3d_8c32_f7579ea79079


# Operator source: {"catalog_type": "airflow-provider-package-catalog", "component_ref": {"provider_package": "apache_airflow_providers_papermill-2.2.3-py3-none-any.whl", "provider": "apache_airflow_providers_papermill", "file": "airflow/providers/papermill/operators/papermill.py"}}
op_0cb3a3d9_a185_425a_8f32_0bb85a5dd819 = PapermillOperator(
    task_id="Part_2___Data_Analysis_ipynb",
    input_nb="Part 2 - Data Analysis.ipynb",
    output_nb="Part 2 - Data Analysis_out.ipynb",
    parameters={},
    kernel_name="",
    dag=dag,
)

op_0cb3a3d9_a185_425a_8f32_0bb85a5dd819 << op_0a1b4861_a7b3_4b5c_a1be_8f2f0fb25d88


# Operator source: {"catalog_type": "airflow-provider-package-catalog", "component_ref": {"provider_package": "apache_airflow_providers_papermill-2.2.3-py3-none-any.whl", "provider": "apache_airflow_providers_papermill", "file": "airflow/providers/papermill/operators/papermill.py"}}
op_ad0925be_c5a3_4551_bdf0_2e6240299cb7 = PapermillOperator(
    task_id="Part_3___Time_Series_Forecasting_ipynb",
    input_nb="Part 3 - Time Series Forecasting.ipynb",
    output_nb="Part 3 - Time Series Forecasting_out.ipynb",
    parameters={},
    kernel_name="",
    dag=dag,
)

op_ad0925be_c5a3_4551_bdf0_2e6240299cb7 << op_0a1b4861_a7b3_4b5c_a1be_8f2f0fb25d88
