import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "qa-secret-key"

def init_db():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE,
            senha TEXT
        )
    """)
    # Insere usuário padrão se não existir
    cursor.execute("INSERT OR IGNORE INTO usuarios (usuario, senha) VALUES (?, ?)", ("admin", "123456"))
    conn.commit()
    conn.close()

@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
    user = cursor.fetchone()
    conn.close()

    if user:
        return f"<h1>Bem-vindo, {usuario}! Login realizado com sucesso.</h1>"
    else:
        flash("Usuário ou senha inválidos.")
        return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)