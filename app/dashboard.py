import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Cache data so it only loads once ──────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv(BASE_DIR / "data" / "data.csv")
    df = df.rename(columns={'time': 'datetime'})
    df['datetime'] = pd.to_datetime(df['datetime'], format='mixed', dayfirst=False)
    df.set_index('datetime', inplace=True)
    return df

# ── Cache models so they only load once ───────────────────────────────────
@st.cache_resource
def load_models():
    model         = joblib.load(BASE_DIR / "models" / "model.pkl")
    anomaly_model = joblib.load(BASE_DIR / "models" / "anomaly.pkl")
    return model, anomaly_model

# ── Load everything ────────────────────────────────────────────────────────
with st.spinner("Loading data and models..."):
    df = load_data()
    model, anomaly_model = load_models()

# ── Dashboard ──────────────────────────────────────────────────────────────
st.title("⚡ Smart Electricity Dashboard")

st.subheader("Global Active Power Over Time")
st.line_chart(df['global_active_power'])

# ── Prediction ─────────────────────────────────────────────────────────────
st.subheader("📈 Predict Usage")
hour  = st.slider("Hour",  0, 23)
day   = st.slider("Day",   1, 31)
month = st.slider("Month", 1, 12)

if st.button("Predict"):
    pred = model.predict([[hour, day, month]])
    st.success(f"Predicted Usage: {pred[0]:.4f} kW")

# ── Anomalies ──────────────────────────────────────────────────────────────
if 'anomaly' in df.columns:
    anomalies = df[df['anomaly'] == -1]
    st.write("### ⚠️ Anomalies Detected")
    st.dataframe(anomalies)