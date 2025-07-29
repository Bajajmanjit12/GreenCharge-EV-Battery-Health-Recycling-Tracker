from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('battery_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS battery (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            battery_id TEXT,
            charge_cycles INTEGER,
            voltage REAL,
            degradation REAL,
            date_logged TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('battery_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM battery ORDER BY date_logged DESC")
    data = c.fetchall()
    conn.close()
    return render_template('dashboard.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    battery_id = request.form['battery_id']
    charge_cycles = int(request.form['charge_cycles'])
    voltage = float(request.form['voltage'])
    degradation = float(request.form['degradation'])

    conn = sqlite3.connect('battery_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO battery (battery_id, charge_cycles, voltage, degradation, date_logged) VALUES (?, ?, ?, ?, ?)",
              (battery_id, charge_cycles, voltage, degradation, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
