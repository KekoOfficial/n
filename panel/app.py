from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_users():
    conn = sqlite3.connect("khasam.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route("/")
def home():
    key = request.args.get("key")
    if key != "khasam123":
        return "Acceso denegado"
    users = get_users()
    html = "<h1>👑 KHASAM PANEL</h1>"
    for u in users:
        html += f"<p>ID: {u[1]} | User: {u[2]} | Usos: {u[3]}</p>"
    return html

app.run(host="0.0.0.0", port=5000)