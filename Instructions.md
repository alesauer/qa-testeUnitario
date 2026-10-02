# Instructions.md

Guia prático e passo a passo para configuração do ambiente, execução da aplicação e execução dos testes de QA.

---

## 🌐 Ambientes da Aplicação

- **Produção / Online:** [https://qa.sauer.pro.br](https://qa.sauer.pro.br)
- **Documentação & Laboratório JMeter:** [https://qa.sauer.pro.br/documentacao](https://qa.sauer.pro.br/documentacao)
- **Local (Docker Compose):** `http://localhost:5555`
- **Local (Python direto):** `http://localhost:5000`

---

## 1. Pré-requisitos

- Python 3.11+ e `pip`
- Docker & Docker Compose (opcional para execução conteinerizada)
- Java JRE/JDK 8+ (para executar o Apache JMeter)
- Node.js + npm (opcional, caso queira rodar `newman`)

---

## 2. Instalação e Execução Local

### Opção A: Executar com Python (Sem Docker)

```bash
# 1. Criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate       # No Windows
# source .venv/bin/activate  # No Linux/Mac

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Executar o servidor
python app.py
```
Acesse: [http://localhost:5000](http://localhost:5000)

---

### Opção B: Executar via Docker Compose

```bash
docker compose up -d --build
```
Acesse: [http://localhost:5555](http://localhost:5555)

---

## 3. Execução dos Testes Automatizados (Pytest)

Para rodar todos os testes de unidade e integração:

```bash
pytest -v
```

---

## 4. Testes de Carga e Stress com Apache JMeter

O projeto já inclui um plano pronto: `teste_login_jmeter.jmx`.

1. Abra o Apache JMeter (`bin/jmeter.bat` no Windows).
2. Vá em **File ➔ Open** e selecione o arquivo `teste_login_jmeter.jmx`.
3. O plano já vem configurado para testar o endpoint `https://qa.sauer.pro.br/login`.
4. Clique no botão verde **▶ (Start)** para iniciar a execução.
5. Acompanhe os resultados nos ouvintes:
   - **View Results Tree:** Ver detalhes de cada requisição.
   - **Summary Report:** Métricas de latência média, vazão (throughput) e taxa de erros.

---

## 5. Testes de API com Postman / Newman

Execute a coleção via CLI com o Newman:

```bash
npm install -g newman
newman run test_postman.json --delay-request 50
```

---

## 6. Credenciais de Teste

- **Usuário:** `admin`
- **Senha:** `123456`
