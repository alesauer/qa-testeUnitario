import os
import sqlite3
import pytest
from app import app, init_db

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False

    # Garante que o banco e o usuário padrão existam antes do teste
    init_db()

    with app.test_client() as client:
        yield client

    # Limpeza opcional após os testes
    if os.path.exists("banco.db"):
        os.remove("banco.db")

def test_pagina_login_carrega_com_sucesso(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Sistema Login QA" in response.get_data(as_text=True)

def test_login_sucesso(client):
    dados = {
        "usuario": "admin",
        "senha": "123456"
    }
    response = client.post("/login", data=dados, follow_redirects=True)
    assert response.status_code == 200
    assert "Bem-vindo, admin!" in response.get_data(as_text=True)

def test_login_falha_senha_incorreta(client):
    dados = {
        "usuario": "admin",
        "senha": "senha_errada"
    }
    response = client.post("/login", data=dados, follow_redirects=True)
    assert response.status_code == 200
    assert "Usuário ou senha inválidos." in response.get_data(as_text=True)

def test_login_falha_usuario_inexistente(client):
    dados = {
        "usuario": "inexistente",
        "senha": "123"
    }
    response = client.post("/login", data=dados, follow_redirects=True)
    assert response.status_code == 200
    assert "Usuário ou senha inválidos." in response.get_data(as_text=True)