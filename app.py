from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS lifecycle
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  battery_id TEXT,
                  action TEXT,
                  location TEXT,
                  date TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Home route
@app.route('/')
def home():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lifecycle ORDER BY date DESC")
    logs = c.fetchall()
    conn.close()
    return render_template('lifecycle.html', logs=logs)

# Add log
@app.route('/add', methods=['POST'])
def add_log():
    battery_id = request.form['battery_id']
    action = request.form['action']
    location = request.form['location']
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO lifecycle (battery_id, action, location, date) VALUES (?, ?, ?, ?)",
              (battery_id, action, location, date))
    conn.commit()
    conn.close()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
