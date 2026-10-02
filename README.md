# Sistema Login QA

Aplicação para autenticação de usuários desenvolvida para estudos e práticas de Garantia da Qualidade de Software (QA), cobrindo testes unitários, testes de integração, testes de API (Postman/Newman) e testes de Carga e Stress (Apache JMeter).

---

## 🌐 Ambiente Online

A aplicação está disponível publicamente para testes e demonstrações em:
- **URL Oficial:** [https://qa.sauer.pro.br](https://qa.sauer.pro.br)
- **Documentação e Laboratórios:** [https://qa.sauer.pro.br/documentacao](https://qa.sauer.pro.br/documentacao)

---

## 🛠️ Tecnologias Utilizadas

- **Frontend:** HTML5, Tailwind CSS (via CDN), Jinja2
- **Backend:** Python 3.11, Flask
- **Banco de Dados:** SQLite
- **Testes de Desempenho:** Apache JMeter (Testes de Carga e Stress)
- **Testes Automatizados:** Pytest, Postman, Newman
- **DevOps:** Docker, Docker Compose, Proxy Reverso com SSL (HTTPS)

---

## 📁 Estrutura de Arquivos

```text
AuthQA-TesteCargaStress/
├── templates/
│   ├── login.html              # Interface de login com Tailwind
│   └── documentacao.html       # Portal com arquitetura, APIs e guia do JMeter
├── app.py                      # Aplicação Flask e manipulação do SQLite
├── banco.db                    # Banco de dados local (gerado dinamicamente)
├── teste_login_jmeter.jmx      # Plano de testes do Apache JMeter pronto para uso
├── test_app.py                 # Testes automatizados com Pytest
├── test_postman.json           # Coleção de testes para o Postman/Newman
├── requirements.txt            # Dependências Python (Flask, pytest)
├── Dockerfile                  # Receita de build da imagem Docker
├── docker-compose.yml          # Orquestração do container (porta 5555:5000)
├── Instructions.md             # Guia passo a passo de configuração e execução
└── README.md                   # Documentação do projeto
```

---

## 🔑 Credenciais Padrão de Teste

- **Usuário:** `admin`
- **Senha:** `123456`