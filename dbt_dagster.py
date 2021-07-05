from dagster import pipeline
from dagster_dbt import dbt_cli_run

config = {"project-dir": "/Users/NavneetSajwan/Desktop/simple_dbt_project/"}
run_all_models = dbt_cli_run.configured(config, name="run_dbt_project")

@pipeline
def my_dbt_pipeline():
    run_all_models()