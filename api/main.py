from fastapi import FastAPI
import joblib
import numpy as np
from pathlib import Path
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (important for Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fix path
BASE_DIR = Path(__file__).resolve().parent

print("Loading models...")

model = joblib.load(BASE_DIR / "models" / "model.pkl")
anomaly_model = joblib.load(BASE_DIR / "models" / "anomaly.pkl")

print("Models loaded successfully ✅")

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("api.main:app", host="0.0.0.0", port=port)