from flask import Flask, request, redirect, render_template, url_for, session, send_from_directory
import os
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '147369'
app.config['MYSQL_DB'] = 'filedb'

# Fake user database (for login)
users = {
    "admin": "123456"
}

# Upload folder setup
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

mysql = MySQL(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM files")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', files=data)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'username' not in session:
        return redirect(url_for('login'))

    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO files (filename, filepath) VALUES (%s, %s)", (file.filename, filepath))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    if 'username' not in session:
        return redirect(url_for('login'))
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
