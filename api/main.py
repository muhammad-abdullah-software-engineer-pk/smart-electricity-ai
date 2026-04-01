from fastapi import FastAPI
import joblib
import numpy as np
from pathlib import Path

app = FastAPI()

# Build absolute paths relative to this file's location
BASE_DIR = Path(__file__).resolve().parent.parent  # points to smart-electricity-ai/

model = joblib.load(BASE_DIR / "models" / "model.pkl")
anomaly_model = joblib.load(BASE_DIR / "models" / "anomaly.pkl")

@app.get("/")
def home():
    return {"message": "AI Electricity API Running"}

@app.get("/predict")
def predict(hour: int, day: int, month: int):
    data = np.array([[hour, day, month]])
    prediction = model.predict(data)[0]
    return {"prediction": float(prediction)}

@app.get("/detect")
def detect(value: float):
    result = anomaly_model.predict([[value]])[0]
    return {"anomaly": int(result)}