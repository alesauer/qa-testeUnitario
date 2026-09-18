# Sistema Login QA

Aplicação minimalista para autenticação de usuários desenvolvida para fins de estudo e testes de qualidade de software (QA). O projeto inclui interface web com Tailwind CSS, backend em Flask com SQLite, containerização via Docker e suítes de testes automatizados (Pytest e Postman).

---

## 🛠️ Tecnologias Utilizadas

- **Frontend:** HTML5, Tailwind CSS (via CDN)
- **Backend:** Python 3.11, Flask
- **Banco de Dados:** SQLite
- **Testes:** Pytest, Postman
- **DevOps:** Docker, Docker Compose

---

## 📁 Estrutura de Arquivos

```text
meu-projeto/
├── templates/
│   └── login.html                          # Interface de login com Tailwind
├── app.py                                  # Aplicação Flask e manipulação do SQLite
├── requirements.txt                        # Dependências Python (Flask, pytest)
├── Dockerfile                              # Receita de build da imagem Docker
├── docker-compose.yml                      # Orquestração do container
├── test_app.py                             # Testes unitários/integração com Pytest
├── Sistema_Login_QA.postman_collection.json # Suíte de testes para o Postman
└── README.md                               # Documentação do projeto