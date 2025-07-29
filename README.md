# 🔋 GreenCharge – EV Battery Health & Recycling Tracker

**GreenCharge** is a smart and sustainable software platform to track, predict, and share EV battery health and lifecycle for resale, reuse, and recycling.  

> ⚡ Built for Sustainable Mobility & Circular Battery Systems  
> 🌱 Empowering second-life battery use and responsible recycling.

---

## 🌍 Problem

Electric Vehicle (EV) batteries degrade over time, but:

- There's **no clear way to track battery health** for second-hand resale or recycling.
- Many batteries are **discarded early**, even if still reusable.
- Recyclers and buyers have **no reliable data** on battery condition or history.

---

## 🎯 Solution

**GreenCharge** offers a digital ecosystem to:

- 📦 Generate a **Battery Passport** (PDF + QR) with detailed battery health & usage history.
- 📈 Track the **battery lifecycle** from manufacturing to reuse and recycling.
- 🧠 Predict **remaining battery life** using a lightweight AI model.
- 🔐 Provide **role-based dashboards** for Users, Recyclers, Manufacturers, and Admins.

---

## 🛠️ Features

| Feature                     | Description                                                  |
|----------------------------|--------------------------------------------------------------|
| ✅ Battery Health Dashboard | Track charge cycles, voltage, degradation trends             |
| 📄 Battery Passport         | Generate and download a PDF + QR battery report             |
| 🔁 Lifecycle Tracker        | Log resale, reuse, and recycling steps                      |
| 🔐 Role-Based Login         | Separate dashboards for each user type                     |
| 🤖 AI Prediction (Optional) | Estimate remaining battery life using regression models     |
| ☁️ Cloud Sync (Optional)    | Sync data securely using Firebase or MySQL backend          |

---

## 👥 User Roles

| Role          | Access & Features |
|---------------|-------------------|
| 👤 User        | Battery Health + Lifecycle Tracker |
| 🧑‍🔧 Manufacturer | Passport Generator + Lifecycle Log |
| ♻️ Recycler     | Lifecycle Tracker (Recycling) |
| 🛡️ Admin        | Access all dashboards + user management (optional) |

---

## 🖼️ Screenshots (Coming Soon)

- 📊 Battery Health Dashboard  
- 📄 Battery Passport with QR Code  
- 🔁 Lifecycle Timeline View  
- 🔐 Role-based Dashboards  

---

## 🚀 Tech Stack

| Layer        | Tech Used                   |
|--------------|-----------------------------|
| Frontend     | Streamlit / Flask / HTML+CSS |
| Backend      | Python, Flask, SQLite / MySQL |
| Authentication | Flask-Login or Firebase Auth |
| PDF Generator | `reportlab`                 |
| QR Code Tool | `qrcode`                    |
| AI Model     | Scikit-learn or TensorFlow  |
| Deployment   | Streamlit Cloud / Heroku    |

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/greencharge.git
cd greencharge

# 2. Create virtual environment (optional)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```
##  Project structure

greencharge/
├── templates/                   # HTML templates for dashboards
│   ├── login.html
│   ├── register.html
│   ├── user_dashboard.html
│   ├── admin_dashboard.html
│   ├── manufacturer_dashboard.html
│   └── recycler_dashboard.html
├── static/                      # CSS, QR codes, or assets
├── app.py                       # Main app logic (Flask or Streamlit)
├── database.py                  # Database connection logic
├── passport_generator.py        # PDF + QR generation
├── lifecycle.py                 # Lifecycle tracking logic
├── requirements.txt
└── README.md

## ✨ Future Enhancements
📲 Mobile-friendly UI
🌐 Multilingual support (Marathi, Hindi)
🧩 Integration with vehicle OBD systems
📊 Live battery data via APIs or IoT

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss.

📫 Contact
📧 Email: bajajmanjit25@gmail.com
🔗 LinkedIn: (https://www.linkedin.com/in/manjit-bajaj-1839a0281/)

