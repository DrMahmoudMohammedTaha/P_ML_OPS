
from __future__ import annotations
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="mlops_pipeline_with_monitoring",
    start_date=pendulum.datetime(2025, 9, 15, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["mlops", "mlflow", "prometheus"],
) as dag:
    # Task 1: Train the model using MLflow
    # This task runs the train_model.py script from our previous example
    train_model_task = BashOperator(
        task_id="train_model_with_mlflow",
        bash_command="python /path/to/your/train_model.py",
        # Assumes MLflow tracking server is running
    )

    # Task 2: Deploy the trained model from MLflow Registry
    # This task would run a script that fetches the latest model from MLflow
    # and starts the API (api.py) on a server
    deploy_model_task = BashOperator(
        task_id="deploy_model_for_monitoring",
        bash_command="python /path/to/your/api.py &", # "&" runs the process in the background
        # You would use a more robust deployment method in production
    )

    # Task 3: A simple task to signal that monitoring has started
    # Prometheus and Grafana are assumed to be running and configured
    start_monitoring_task = BashOperator(
        task_id="start_monitoring",
        bash_command="echo 'Monitoring has been enabled for the deployed model. Check Prometheus and Grafana dashboards.'",
    )

    # Define the dependencies
    train_model_task >> deploy_model_task >> start_monitoring_task