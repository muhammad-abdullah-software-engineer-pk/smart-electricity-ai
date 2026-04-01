# app/dashboard.py

import streamlit as st
import pandas as pd
import requests
from pathlib import Path

# ── BASE DIRECTORY ─────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent  # points to smart-electricity-ai/

# ── LIVE API URL ───────────────────────────────────────────────────────────
API_URL = "https://smart-electricity-ai--muhammadabdu941.replit.app"

# ── CACHE DATA ─────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    """
    Load historical electricity data from CSV.
    """
    df = pd.read_csv(BASE_DIR / "data" / "data.csv")
    df = df.rename(columns={'time': 'datetime'})
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
    df.set_index('datetime', inplace=True)
    return df

# ── LOAD DATA ──────────────────────────────────────────────────────────────
with st.spinner("Loading historical data..."):
    df = load_data()

# ── DASHBOARD ──────────────────────────────────────────────────────────────
st.title("⚡ Smart Electricity Dashboard")

st.subheader("📊 Global Active Power Over Time")
st.line_chart(df['global_active_power'])

# ── PREDICTION ─────────────────────────────────────────────────────────────
st.subheader("📈 Predict Electricity Usage")

hour  = st.slider("Hour (0-23)", 0, 23)
day   = st.slider("Day (1-31)", 1, 31)
month = st.slider("Month (1-12)", 1, 12)

if st.button("Predict Usage"):
    try:
        response = requests.get(
            f"{API_URL}/predict",
            params={"hour": hour, "day": day, "month": month},
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        st.success(f"Predicted Usage: {data['prediction']:.4f} kWh")
    except requests.exceptions.RequestException as e:
        st.error(f"Error calling API: {e}")

# ── ANOMALY DETECTION ───────────────────────────────────────────────────────
st.subheader("⚠️ Anomaly Detection")

value = st.number_input(
    "Enter value to check for anomaly",
    min_value=0.0,
    max_value=1000.0,
    value=50.0
)

if st.button("Check Anomaly"):
    try:
        response = requests.get(
            f"{API_URL}/detect",
            params={"value": value},
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        if data["anomaly"] == 1:
            st.warning("⚠️ Anomaly detected!")
        else:
            st.success("✅ Value is normal")
    except requests.exceptions.RequestException as e:
        st.error(f"Error calling API: {e}")

# ── OPTIONAL: Display raw anomalies from CSV ────────────────────────────────
if 'anomaly' in df.columns:
    anomalies = df[df['anomaly'] == -1]
    if not anomalies.empty:
        st.write("### ⚠️ Historical Anomalies Detected")
        st.dataframe(anomalies)