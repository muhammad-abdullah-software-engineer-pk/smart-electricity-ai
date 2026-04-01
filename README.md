<div align="center">

# ⚡ Smart Electricity AI System

**A production-ready AI system for electricity consumption prediction and anomaly detection**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

[🔗 Live API](#) · [📊 Live Dashboard](#) · [📖 Documentation](#-table-of-contents)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Machine Learning](#-machine-learning)
- [API Endpoints](#-api-endpoints)
- [Installation](#-installation--setup)
- [Running the Project](#-running-the-project)
- [Dependencies](#-dependencies)
- [Challenges & Solutions](#-challenges--solutions)
- [Future Improvements](#-future-improvements)

---

## 🚀 Overview

Smart Electricity AI is a full-stack intelligent system that:

- **Predicts** electricity consumption using historical usage patterns
- **Detects anomalies** such as sudden spikes or potential electricity theft
- **Exposes predictions** through a live REST API (FastAPI)
- **Visualizes** everything through an interactive web dashboard (Streamlit)

> Built for real-world deployment on cloud platforms like Replit and Streamlit Cloud.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📈 **Usage Prediction** | Forecast electricity consumption by hour, day, and month |
| ⚠️ **Anomaly Detection** | Identify suspicious spikes or unusual patterns |
| 🌐 **Live REST API** | FastAPI backend with auto-generated Swagger docs |
| 📊 **Interactive Dashboard** | Real-time Streamlit UI with charts and controls |
| ☁️ **Cloud Ready** | Deployable on Replit (API) + Streamlit Cloud (UI) |

---

## 🏗️ System Architecture

```
User  →  Streamlit Dashboard  →  FastAPI Backend  →  ML Models
```

| Layer | Technology | Role |
|---|---|---|
| **Frontend** | Streamlit | UI, charts, user input |
| **Backend** | FastAPI | REST endpoints, routing |
| **Prediction** | Linear Regression | Consumption forecasting |
| **Anomaly** | Isolation Forest | Outlier / theft detection |

---

## 📂 Project Structure

```
SMART-ELECTRICITY-AI/
│
├── api/
│   └── main.py              # FastAPI backend – all REST endpoints
│
├── app/
│   └── dashboard.py         # Streamlit dashboard – UI & visualizations
│
├── data/
│   └── data.csv             # Dataset for model training
│
├── models/
│   ├── model.pkl            # Trained Linear Regression model
│   └── anomaly.pkl          # Trained Isolation Forest model
│
├── notebooks/
│   └── eda.ipynb            # Exploratory data analysis
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🧠 Machine Learning

### 🔹 Prediction Model

- **Algorithm:** Linear Regression
- **Input Features:**
  - `hour` — Hour of the day (0–23)
  - `day` — Day of the month (1–31)
  - `month` — Month of the year (1–12)
- **Output:** Predicted electricity usage in **kWh**
- **Stored as:** `models/model.pkl`

### 🔹 Anomaly Detection Model

- **Algorithm:** Isolation Forest
- **Detects:**
  - Sudden consumption spikes
  - Unusual usage patterns (potential theft)
- **Output:** `1` = Anomaly | `-1` = Normal
- **Stored as:** `models/anomaly.pkl`

---

## ⚙️ API Endpoints

### `GET /predict` — Forecast electricity usage

```http
GET /predict?hour=10&day=15&month=6
```

**Response:**
```json
{
  "prediction": 1.23
}
```

---

### `GET /detect` — Detect anomaly

```http
GET /detect?value=50
```

**Response:**
```json
{
  "anomaly": 1
}
```

> 📘 Interactive API docs available at `http://127.0.0.1:8000/docs`

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/muhammad-abdullah-software-engineer-pk/smart-electricity-ai.git
cd smart-electricity-ai
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

**Activate:**

```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 🚀 Start the FastAPI Backend

```bash
uvicorn api.main:app --reload
```

Then open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 📊 Start the Streamlit Dashboard

```bash
streamlit run app/dashboard.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---

### 🔗 Connect Dashboard to API

In `app/dashboard.py`, set the API URL:

```python
# Local development
API_URL = "http://127.0.0.1:8000"

# Production
API_URL = "your-live-api-url"
```

---

## 📦 Dependencies

```txt
fastapi
uvicorn
streamlit
pandas
numpy
scikit-learn
joblib
requests
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🚧 Challenges & Solutions

| Problem | Solution |
|---|---|
| API not responding | Fixed dynamic port configuration |
| JSON parse errors | Debugged API response formatting |
| Model path issues | Switched to absolute file paths |
| Slow dashboard renders | Implemented caching & optimized charts |

---

## 🔮 Future Improvements

- [ ] **LSTM Neural Network** — improve time-series prediction accuracy
- [ ] **Real-Time IoT Integration** — connect live smart-meter data streams
- [ ] **Alert System** — SMS and email notifications on anomaly detection
- [ ] **Mobile App** — extend access to Android and iOS platforms

---

## 🌐 Live Demo

| Service | Link |
|---|---|
| 🔗 API | *(your Replit link here)* |
| 📊 Dashboard | *(your Streamlit Cloud link here)* |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**⚡ Smart Electricity AI — Built for the Future of Energy Management**

[Muhammad Abdullah](https://github.com/muhammad-abdullah-software-engineer-pk)

</div>
