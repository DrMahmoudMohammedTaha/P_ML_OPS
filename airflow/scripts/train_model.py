import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

# Set up MLflow tracking
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("Model Monitoring Example")

# Start an MLflow run
with mlflow.start_run() as run:
    # 1. Prepare data
    data = pd.DataFrame({
        "feature1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "feature2": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "target": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    })
    X = data[["feature1", "feature2"]]
    y = data["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 2. Train the model
    n_estimators = 100
    model = RandomForestClassifier(n_estimators=n_estimators)
    model.fit(X_train, y_train)

    # 3. Log parameters and metrics with MLflow
    mlflow.log_param("n_estimators", n_estimators)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    mlflow.log_metric("accuracy", accuracy)
    print(f"Model accuracy: {accuracy}")

    # 4. Save the model to the MLflow Model Registry
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="random-forest-model",
        registered_model_name="MyRFModel"
    )

print(f"MLflow Run ID: {run.info.run_id}")