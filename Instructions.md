# Instructions.md

Guia prático e passo a passo para configurar o ambiente, executar a aplicação e rodar os testes.

---

## Pré-requisitos

- Windows com WSL2 habilitado (recomendado) ou outro SO compatível
- Python 3.11 e `pip`
- Docker & Docker Compose (opcional, recomendado)
- Node.js + npm (opcional, para `newman`)

### Instalar Docker Desktop (Windows)
1. Baixe em: https://www.docker.com/products/docker-desktop/
2. Execute o instalador e marque **Use WSL 2** quando solicitado.
3. Reinicie a máquina se necessário.
4. Abra o Docker Desktop e aguarde "Engine running".

---

## Instalar dependências Python (local)

No diretório do projeto, crie um virtualenv (recomendado) e instale as dependências:

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows PowerShell/CMD use .venv\\Scripts\\activate
pip install -r requirements.txt
```

---

## Rodar a aplicação localmente (sem Docker)

```bash
python app.py
# ou
flask run --host=0.0.0.0 --port=5000
```

Acesse: http://localhost:5000 (ou 5000 via `docker-compose` mapeado para 5555 — veja abaixo).

---

## Rodar com Docker (build e run)

```bash
docker build -t sistema-login-qa .
docker run -p 5555:5000 --rm sistema-login-qa
```

Isso expõe a aplicação em http://localhost:5555

---

## Rodar com Docker Compose

O projeto já contém `docker-compose.yml` que mapeia a porta `5555` para a porta `5000` do container.

```bash
docker-compose up --build
```

Acesse: http://localhost:5555/

---

## Executar os testes (Pytest)

```bash
pytest -q
```

Observação: os testes usam/geram `banco.db`. O fixture `client` remove `banco.db` ao final dos testes locais.

---

## Executar coleção Postman com Newman (opcional)

Instale o `newman` globalmente (se desejar rodar a suíte Postman a partir da CLI):

```bash
npm install -g newman
newman run test_postman.json --delay-request 50
```

Os requests da coleção usam `http://localhost:5555` por padrão.

---

## Variáveis de ambiente e configurações úteis

- `SECRET_KEY` (recomendado): não comitar `app.secret_key` em produção. Você pode exportar:

```bash
set SECRET_KEY="sua_chave_segura"        # Windows
export SECRET_KEY="sua_chave_segura"     # Linux/Mac
```

No `app.py` pode-se preferir buscar `os.environ.get('SECRET_KEY')`.

---

## Reset / seed do banco

Para resetar o banco localmente:

```bash
rm banco.db            # ou del banco.db no Windows
python -c "from app import init_db; init_db()"
```

O `init_db()` cria a tabela `usuarios` e insere o usuário padrão `admin` com senha `123456` (apenas para QA/demonstração).

---

## Notas de segurança e recomendações

- Não armazene senhas em texto plano; use hashing (`werkzeug.security` ou `bcrypt`).
- Não versionar `banco.db`; adicione-o ao `.gitignore`.
- Use `SECRET_KEY` via variável de ambiente para sessões/flash messages.
- Para ambiente de produção, avalie usar migrações (Alembic/Flask-Migrate) e um banco mais robusto.

---

Se quiser, posso atualizar automaticamente o `app.py` para usar hashing de senha, adicionar `.gitignore` e executar os testes aqui.
# Instructions.md

Guia prático e passo a passo para configuração do ambiente, execução da aplicação e testes.

---

## 1. Pré-requisito: Instalação do Docker

Se você ainda não possui o Docker e o Docker Compose instalados na sua máquina, siga as instruções para o seu sistema operacional:

### Windows
1. Baixe o instalador oficial do **Docker Desktop**:
   - [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Execute o arquivo `.exe` baixado e siga as instruções na tela.
3. Certifique-se de marcar a opção **Use WSL 2** durante a instalação.
4. Reinicie o computador após a conclusão da instalação.
5. Abra o aplicativo **Docker Desktop** e aguarde até que o status no canto inferior esquerdo indique "Engine running".



