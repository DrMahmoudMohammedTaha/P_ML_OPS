import os
from pathlib import Path

# Define the root directory for your project
project_name = r"C:\Users\Mahmoud_Taha\Desktop\new-project"
root_dir = Path(project_name)

# Define the folder structure as a list of paths
folder_structure = [
    "airflow/dags",
    "airflow/scripts",
    "data/raw",
    "data/processed",
    "prometheus",
    "grafana/dashboards",
    "grafana/provisioning"
]

# Create the root directory
os.makedirs(root_dir, exist_ok=True)

# Create all the nested directories
for path in folder_structure:
    (root_dir / path).mkdir(parents=True, exist_ok=True)

# Create placeholder files to complete the structure
placeholder_files = [
    "airflow/dags/mlops_dag.py",
    "airflow/scripts/train_model.py",
    "airflow/scripts/api.py",
    "prometheus/prometheus.yml",
    "grafana/provisioning/datasources.yml",
    "docker-compose.yml",
    "requirements.txt"
]

for file_path in placeholder_files:
    (root_dir / file_path).touch(exist_ok=True)

print(f"Project structure '{project_name}' created successfully.")