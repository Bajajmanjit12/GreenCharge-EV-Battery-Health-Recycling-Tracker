# app.py
from flask import Flask, render_template, request, redirect, session, send_file
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_session import Session
from config import DB_CONFIG
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL config
app.config['MYSQL_HOST'] = DB_CONFIG['host']
app.config['MYSQL_USER'] = DB_CONFIG['user']
app.config['MYSQL_PASSWORD'] = DB_CONFIG['password']
app.config['MYSQL_DB'] = DB_CONFIG['database']

# Session config
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

mysql = MySQL(app)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

# ---------- Auth Routes ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)",
                    (username, email, hashed_password, role))
        mysql.connection.commit()
        cur.close()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password_input = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, username, password, role FROM users WHERE email=%s", (email,))
        user = cur.fetchone()
        cur.close()
        if user and bcrypt.check_password_hash(user[2], password_input):
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['role'] = user[3]
            return redirect('/dashboard')
        else:
            return 'Login Failed'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# ---------- Dashboard ----------
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/login')

    role = session.get('role', '').strip().lower()
    username = session['username']

    if role == 'user':
        return render_template('dashboard_user.html', username=username)
    elif role == 'admin':
        return render_template('dashboard_admin.html', username=username)
    elif role == 'manufacturer':
        return render_template('dashboard_manufacturer.html', username=username)
    elif role == 'recycler':
        return render_template('dashboard_recycler.html', username=username)
    else:
        return "Unauthorized role: " + repr(role), 403

# ---------- Battery Passport ----------
@app.route('/passport')
def passport():
    if 'username' not in session:
        return redirect('/login')
    return render_template('passport.html')

@app.route('/generate_passport')
def generate_passport():
    if 'username' not in session:
        return redirect('/login')

    battery_info = {
        "Battery ID": "EVB-987654",
        "Manufacturer": "EcoVolt",
        "Charge Cycles": 540,
        "Voltage": "400V",
        "State of Health": "85%",
        "Last Updated": datetime.date.today().strftime("%Y-%m-%d")
    }

    # 1. Generate PDF
    os.makedirs("static", exist_ok=True)
    pdf_filename = f"{battery_info['Battery ID']}_passport.pdf"
    pdf_path = os.path.join("static", pdf_filename)

    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "Battery Passport")
    c.setFont("Helvetica", 12)
    y = 710
    for key, value in battery_info.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 30

    # 2. QR Code
    qr_url = f"http://127.0.0.1:5000/download/{pdf_filename}"
    qr_img = qrcode.make(qr_url)
    qr_path = os.path.join("static", "qr_codes", f"{battery_info['Battery ID']}_qr.png")
    os.makedirs(os.path.dirname(qr_path), exist_ok=True)
    qr_img.save(qr_path)

    # 3. Embed QR in PDF
    c.drawImage(qr_path, 400, 600, width=150, height=150)
    c.save()

    return render_template("passport.html", pdf=pdf_filename, qr=f"static/qr_codes/{battery_info['Battery ID']}_qr.png")

@app.route('/lifecycle', methods=['GET', 'POST'])
def lifecycle():
    if 'user_id' not in session:
        return redirect('/login')

    cur = mysql.connection.cursor()

    if request.method == 'POST':
        battery_id = request.form['battery_id']
        event_type = request.form['event_type']
        event_date = request.form['event_date']
        description = request.form['description']
        user_id = session['user_id']

        cur.execute("""
            INSERT INTO lifecycle_logs (battery_id, event_type, event_date, description, user_id)
            VALUES (%s, %s, %s, %s, %s)
        """, (battery_id, event_type, event_date, description, user_id))
        mysql.connection.commit()

    cur.execute("SELECT * FROM lifecycle_logs ORDER BY event_date DESC")
    events = cur.fetchall()
    cur.close()

    return render_template('lifecycle.html', events=events)

@app.route('/battery-health')
def battery_health():
    if 'username' not in session:
        return redirect('/login')

    # Dummy battery data – replace with MySQL fetch later if needed
    battery_data = {
        "battery_id": "EVB-987654",
        "voltage": "398V",
        "charge_cycles": 540,
        "health_percent": 85
    }

    return render_template('battery_health.html', battery=battery_data)

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join("static", filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
