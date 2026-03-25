import sqlite3

conn = sqlite3.connect("khasam.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    username TEXT,
    usos INTEGER DEFAULT 0
)
""")
conn.commit()

def registrar_usuario(user_id, username):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO users (user_id, username, usos) VALUES (?, ?, 1)",
                       (user_id, username))
    else:
        cursor.execute("UPDATE users SET usos = usos + 1 WHERE user_id=?", (user_id,))
    conn.commit()