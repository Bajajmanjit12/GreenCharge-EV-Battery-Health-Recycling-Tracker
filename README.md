# 🔋 GreenCharge – EV Battery Health & Recycling Tracker

A smart and sustainable software platform to track, predict, and share EV battery health and lifecycle for resale, reuse, and recycling.  

> ⚡ Built for Sustainable Mobility & Circular Battery Systems

---

## 🌍 Problem

Electric Vehicle (EV) batteries degrade over time, but:
- There’s **no clear way to track battery health** for second-hand resale or recycling.
- Many batteries are **discarded early**, even if reusable.
- Recyclers and buyers have **no reliable data** on battery condition or usage history.

---

## 🎯 Solution

**GreenCharge** provides a digital platform that:
- 📦 Generates a **Battery Passport** (PDF/QR) with detailed health and history.
- 📈 Tracks **battery lifecycle** from use to reuse/recycle.
- 🧠 Predicts **remaining battery life** using a lightweight AI model.
- 🔐 Provides **role-based access** for Users, Recyclers, and Manufacturers.

---

## 🛠️ Features

| Feature | Description |
|--------|-------------|
| ✅ Battery Health Dashboard | Track charge cycles, voltage, degradation trends |
| 📄 Battery Passport Generator | Generate PDF + QR with full history |
| 🔁 Lifecycle Tracker | Log resale, reuse, recycling steps |
| 🔒 Role-based Login | Different dashboards for users/recyclers/manufacturers |
| 🤖 AI Prediction (Optional) | Forecast remaining battery life |
| ☁️ Cloud Sync | Store battery history securely (Firebase/MySQL) |

---

## 🖼️ Screenshots (Coming Soon)

> Add screenshots of:  
> - Battery dashboard  
> - Passport PDF  
> - Lifecycle timeline  

---

## 🚀 Tech Stack

| Layer | Tech Used |
|-------|-----------|
| Frontend | Streamlit / Flask / React (Simple UI) |
| Backend | Python, SQLite / Firebase |
| Auth & Roles | Firebase Auth or Flask-Login |
| ML Model | Scikit-learn / TensorFlow (Regression) |
| Extras | `qrcode`, `reportlab` (for PDFs) |

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/greencharge.git
cd greencharge

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
