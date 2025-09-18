

train model:
acitivate py310M
python airflow/scripts/train_model.py

airflow model api:
activate py310M
python airflow\scripts\api.py

start mlflow:
mlflow ui --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000

start docker:
docker compose up --build


test prediction:
curl -X POST http://127.0.0.1:5001/predict -H "Content-Type: application/json" -d "{\"feature1\": 5, \"feature2\": 6}"



========================

Key URLs:
MLflow: http://localhost:5000
API: http://localhost:5001/predict
Prometheus: http://localhost:9090
Grafana: http://localhost:3000

