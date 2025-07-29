from flask import Flask, render_template, request, redirect, session, flash
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_session import Session
from config import DB_CONFIG

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'

# MySQL config
app.config['MYSQL_HOST'] = DB_CONFIG['host']
app.config['MYSQL_USER'] = DB_CONFIG['user']
app.config['MYSQL_PASSWORD'] = DB_CONFIG['password']
app.config['MYSQL_DB'] = DB_CONFIG['database']

Session(app)
mysql = MySQL(app)
bcrypt = Bcrypt(app)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        role = request.form['role']

        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)",
                (username, email, password, role)
            )
            mysql.connection.commit()
            cur.close()
            flash('✅ Registration successful!')
            return redirect('login.html')
        except Exception as e:
            print("❌ MySQL Insert Error:", e)
            flash('❌ Registration failed. Check terminal for error.')

    return render_template('register.html')

@app.route('login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_input = request.form['password']
        role_input = request.form['role']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()

        if user and bcrypt.check_password_hash(user[3], password_input) and user[4] == role_input:
            session['user'] = user[1]
            session['role'] = user[4]
            flash('Login successful')
            return redirect('user_dashboard.html')
        else:
            flash('Invalid login.')
    return render_template('login.html')

@app.route('user_dashboard.html')
def user_dashboard():
    if 'user' in session:
        return render_template('user_dashboard.html', eco_points=0)
    return redirect('login.html')

@app.route('logout.html')
def logout():
    session.clear()
    return redirect('login.html')

if __name__ == '__main__':
    app.run(debug=True)
