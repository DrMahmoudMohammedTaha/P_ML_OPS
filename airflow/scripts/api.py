
import pandas as pd
from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Counter, Gauge
import mlflow.pyfunc

# Load the model from MLflow Model Registry
model_name = "MyRFModel"
model_version = 1  # Get the latest version from the registry in a real-world project
model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")

# Start the Prometheus metrics server
start_http_server(8000)

# Define Prometheus metrics
REQUEST_COUNT = Counter('api_requests_total', 'Total number of API requests.')
PREDICTION_LATENCY = Gauge('prediction_latency_seconds', 'Time taken for a prediction.')

# Create the Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    REQUEST_COUNT.inc()  # Increment the request counter
    
    data = request.json
    start_time = pd.Timestamp.now()
    
    # Preprocess and make a prediction
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df)
    
    end_time = pd.Timestamp.now()
    latency = (end_time - start_time).total_seconds()
    PREDICTION_LATENCY.set(latency)  # Record the prediction latency
    
    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)