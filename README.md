# 🗂️ Flask File Upload with MySQL and Login Authentication

This is a simple full-stack web application built with **Flask**, which allows users to:

- Log in (basic auth)
- Upload files to the server
- Store file info in a **MySQL** database
- Download uploaded files
- Restrict access only to authenticated users

## 🚀 Features

- ✅ User login system (session-based)
- ✅ File upload & storage (in local `uploads/` folder)
- ✅ File metadata saved to MySQL
- ✅ File download via web interface
- ✅ Protected routes (upload/view/download require login)
- ✅ Simple and clean HTML templates
  
## 🛠️ Tech Stack

- **Backend**: Python, Flask, MySQL
- **Frontend**: HTML (Jinja templates)
- **Database**: MySQL (with `flask_mysqldb`)
- **Deployment target**: Localhost or any Python-compatible server

## 🧰 Requirements

- Python 3.8+
- MySQL Server
- pip (Python package manager)

## 📦 Installation & Setup

### 1. Clone this repo

### 2. Install dependencies

```bash
pip install flask flask-mysqldb
```

### 3. Setup MySQL

Login to MySQL and run:

```sql
CREATE DATABASE filedb;
USE filedb;

CREATE TABLE files (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255),
    filepath VARCHAR(500)
);
```

You can customize your database credentials in `app.py`:

```python
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
```

---

## ▶️ Run the App

```bash
python app.py
```

Then open in your browser:

```
http://localhost:5000
```

Or from another device on the same Network:

```
http://your-local-ip:5000
```

---

## 👤 Login Credentials

* Username: `admin`
* Password: `123456`

*(Credentials are hardcoded in `app.py`, you can modify or extend this to MySQL users later.)*

## 📥 Upload & Download

* Upload a file using the form
* Files are stored in the `/uploads/` folder
* Metadata (name + path) stored in MySQL
* Download link will appear after upload


## 📬 Contact

I'm just an undergraduate mech engineering student. feel free to contact me via email : alhamdikaradit@gmail.com or business.radityaz.gmail.com

