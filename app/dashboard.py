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
    Load historical electricity data from CSV and set datetime index
    """
    df = pd.read_csv(BASE_DIR / "data" / "data.csv")
    df = df.rename(columns={'time': 'datetime'})
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
    df.set_index('datetime', inplace=True)
    return df

@st.cache_data
def get_anomalies(df):
    """
    Precompute anomalies for faster display
    """
    if 'anomaly' in df.columns:
        return df[df['anomaly'] == -1]
    return pd.DataFrame()

# ── LOAD DATA ──────────────────────────────────────────────────────────────
with st.spinner("Loading historical data..."):
    df = load_data()
    anomalies = get_anomalies(df)

# ── DASHBOARD ──────────────────────────────────────────────────────────────
st.title("⚡ Smart Electricity Dashboard")

# ── HISTORICAL POWER CHART ─────────────────────────────────────────────────
st.subheader("📊 Global Active Power Over Time")

# Resample hourly to reduce points and improve performance
df_resampled = df['global_active_power'].resample('1h').mean()
st.line_chart(df_resampled.tail(500))  # show last 500 points only

# ── PREDICTION FORM ────────────────────────────────────────────────────────
with st.form("predict_form"):
    st.subheader("📈 Predict Electricity Usage")
    hour  = st.slider("Hour (0-23)", 0, 23)
    day   = st.slider("Day (1-31)", 1, 31)
    month = st.slider("Month (1-12)", 1, 12)
    submit_pred = st.form_submit_button("Predict Usage")

    if submit_pred:
        with st.spinner("Calling API..."):
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

# ── ANOMALY DETECTION FORM ─────────────────────────────────────────────────
with st.form("anomaly_form"):
    st.subheader("⚠️ Anomaly Detection")
    value = st.number_input(
        "Enter value to check for anomaly",
        min_value=0.0,
        max_value=1000.0,
        value=50.0
    )
    submit_anomaly = st.form_submit_button("Check Anomaly")

    if submit_anomaly:
        with st.spinner("Checking anomaly..."):
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

# ── HISTORICAL ANOMALIES ───────────────────────────────────────────────────
if not anomalies.empty:
    st.write("### ⚠️ Historical Anomalies Detected")
    st.dataframe(anomalies)