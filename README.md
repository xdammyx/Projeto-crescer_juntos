
# 🌱 Crescer Juntos – API Backend (Django + DRF + PostgreSQL)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![DRF](https://img.shields.io/badge/DRF-3.x-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![Tests](https://img.shields.io/badge/Tests-Pytest%20%2B%20Coverage-brightgreen)
![CI](https://img.shields.io/badge/GitHub%20Actions-CI-blue)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> **Resumo:** API REST para **troca de plantas e jardinagem colaborativa**, conectando usuários que desejam trocar mudas, sementes e conhecimentos, promovendo a sustentabilidade.

---

## 🧭 Sumário
- [Descrição](#-descrição)
- [Funcionalidades](#-funcionalidades)
- [Arquitetura & Stack](#-arquitetura--stack)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação (sem Docker)](#-instalação-sem-docker)
- [Execução](#-execução)
- [Variáveis de Ambiente](#-variáveis-de-ambiente)
- [Docker & Compose](#-docker--compose)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Banco de Dados & Diagramas](#-banco-de-dados--diagramas)
- [Autenticação](#-autenticação)
- [Endpoints Principais](#-endpoints-principais)
- [Exemplos de Requisição](#-exemplos-de-requisição)
- [Testes](#-testes)
- [Documentação (Swagger/Redoc)](#-documentação-swaggerredoc)
- [Boas Práticas & Segurança](#-boas-práticas--segurança)
- [Deploy](#-deploy)
- [Postman](#-postman)
- [Contribuição](#-contribuição)
- [Licença](#-licença)
- [Autoria](#-autoria)

---

## 📖 Descrição
**Crescer Juntos** é um backend em **Django + Django REST Framework** com banco **PostgreSQL**, seguindo boas práticas de **arquitetura limpa**, **ambientes** e **documentação**.

---

## 🚀 Funcionalidades
- 👤 **Usuários**: cadastro, perfil, localização.
- 🌿 **Plantas**: nome popular/científico, origem, família, descrição, imagens.
- 🔄 **Trocas**: solicitação e fluxo de status (*Pendente, Aceito, Recusado*).
- 💬 **Mensagens**: chat básico entre usuários.
- ⭐ **Avaliações**: notas e comentários para reputação.
- ❤️ **Healthcheck**: estado da API.
- 🔐 **Autenticação**: Token ou JWT (opcional e configurável).
- 🌍 **CORS**: preparado para frontend separado.

---

## 🏗️ Arquitetura & Stack
- 🐍 **Python**: 3.12
- 🌐 **Django**: 5.x
- 🧰 **Django REST Framework (DRF)**: 3.x
- 🗄️ **PostgreSQL**: 13+
- 🧪 **Testes**: Pytest + Coverage
- 🐳 **Infra**: Docker + Docker Compose
- 📦 **Dependências sugeridas**:
  - `django-environ` (config via `.env`)
  - `django-cors-headers` (CORS)
  - `drf-spectacular` ou `drf-yasg` (Swagger/Redoc)
  - `djangorestframework-simplejwt` (JWT) ou `rest_framework.authtoken` (Token)

---

## ⚙️ Pré-requisitos
- ✅ Python 3.12+
- ✅ PostgreSQL 13+
- ✅ Git
- ✅ (Opcional) Docker + Docker Compose

---
## 🎨 **Diagramas do Banco de Dados**

### 🧠 **Modelo Conceitual**
![Diagrama Conceitual](docs/diagrama_conceitual.png)

### 📐 **Modelo Lógico**
![Modelo Lógico](docs/modelo_logico.png)

### 🗄️ **Estrutura do Banco (SQL)**
-- Tabela USUARIOS
CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(40) NOT NULL,
    email VARCHAR(80) UNIQUE NOT NULL,
    senha VARCHAR(15) NOT NULL,
    localizacao VARCHAR(100),
    data_cadastro DATE DEFAULT CURRENT_DATE
);

-- Tabela TROCAS
CREATE TABLE trocas (
    id_troca SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    status VARCHAR(15),
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Tabela PLANTAS
CREATE TABLE plantas (
    id_planta SERIAL PRIMARY KEY,
    nome_popular VARCHAR(40),
    tipo VARCHAR(40),
    origem VARCHAR(80),
    familia VARCHAR(50),
    descricao TEXT,
    imagem VARCHAR(150),
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Tabela IMAGENS
CREATE TABLE imagens (
    id_imagem SERIAL PRIMARY KEY,
    url_imagem VARCHAR(150) NOT NULL,
    id_planta INT NOT NULL,
    FOREIGN KEY (id_planta) REFERENCES plantas(id_planta) ON DELETE CASCADE
);

-- Tabela MENSAGENS
CREATE TABLE mensagens (
    id_chat SERIAL PRIMARY KEY,
    mensagem TEXT NOT NULL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Tabela AVALIACAO
CREATE TABLE avaliacao (
    id_avaliacao SERIAL PRIMARY KEY,
    nota DECIMAL(3,1) CHECK (nota >= 0 AND nota <= 10),
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    comentario TEXT,
    id_avaliador INT NOT NULL,
    id_avaliado INT NOT NULL,
    FOREIGN KEY (id_avaliador) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_avaliado) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);


## 🔧 Instalação (sem Docker)

```bash
# Clone o repositório
git clone https://github.com/xdammyx/Projeto-crescer_juntos.git
cd crescer_juntos

# Crie o virtualenv
python -m venv .venv

# Ative o virtualenv
# Windows (PowerShell)
.\.venv\Scripts\Activate
# Linux/Mac
source .venv/bin/activate

# Instale dependências
pip install -r requirements.txt

# Configure variáveis
cp .env.example .env
# Edite o arquivo .env conforme sua máquina
```

---

## ▶️ Execução

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# Acesse: http://127.0.0.1:8000/api/
```

---

## 🔐 Variáveis de Ambiente
Crie `.env` na raiz:

```env
# Django
DJANGO_SECRET_KEY=troque-por-uma-chave-segura
DJANGO_DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1

# CORS (se usar frontend externo)
CORS_ALLOWED_ORIGINS=http://localhost:3000

# PostgreSQL
POSTGRES_DB=crescer_juntos
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# JWT (se usar SimpleJWT)
SIMPLEJWT_ACCESS_LIFETIME_MINUTES=60
SIMPLEJWT_REFRESH_LIFETIME_DAYS=7
```

> **Produção:** use `DJANGO_DEBUG=0`, configure `ALLOWED_HOSTS` e **nunca** publique a `SECRET_KEY`.

---

## 🐳 Docker & Compose

`docker-compose.yml` (modelo alinhado ao projeto):
```yaml
services:
  web:
    build: .
    container_name: crescer_juntos_web
    command: bash -c "python manage.py migrate && gunicorn crescer_juntos.wsgi:application --bind 0.0.0.0:8000"
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db
  db:
    image: postgres:16
    container_name: crescer_juntos_db
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

**Comandos:**
```bash
docker-compose up --build
docker exec -it crescer_juntos_web bash
python manage.py migrate
```

> **Windows:** Se ocorrer erro de permissão, execute `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`.

---

## 📂 Estrutura do Projeto

```text
📂 CRESCER_JUNTOS
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── pytest.ini
├── README.md
├── requirements.txt
├── crescer_juntos
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__
├── main
│   ├── migrations
│   │   └── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates
├── postman
│   └── crescer_juntos.postman_collection.json
├── scripts
└── docs
    ├── diagrama_conceitual.png
    ├── estrutura_banco.sql
    └── modelo_logico.png
```

---

## 🗄️ Banco de Dados & Diagramas

### 🧠 **Modelo Conceitual**
![Diagrama Conceitual](docs/diagrama_conceitual.png)

### 📐 **Modelo Lógico**
![Modelo Lógico](docs/modelo_logico.png)

### 🗄️ **Estrutura do Banco (SQL)**
-- Tabela USUARIOS
CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(40) NOT NULL,
    email VARCHAR(80) UNIQUE NOT NULL,
    senha VARCHAR(15) NOT NULL,
    localizacao VARCHAR(100),
    data_cadastro DATE DEFAULT CURRENT_DATE
);

-- Tabela TROCAS
CREATE TABLE trocas (
    id_troca SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    status VARCHAR(15),
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Tabela PLANTAS
CREATE TABLE plantas (
    id_planta SERIAL PRIMARY KEY,
    nome_popular VARCHAR(40),
    tipo VARCHAR(40),
    origem VARCHAR(80),
    familia VARCHAR(50),
    descricao TEXT,
    imagem VARCHAR(150),
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Tabela IMAGENS
CREATE TABLE imagens (
    id_imagem SERIAL PRIMARY KEY,
    url_imagem VARCHAR(150) NOT NULL,
    id_planta INT NOT NULL,
    FOREIGN KEY (id_planta) REFERENCES plantas(id_planta) ON DELETE CASCADE
);

-- Tabela MENSAGENS
CREATE TABLE mensagens (
    id_chat SERIAL PRIMARY KEY,
    mensagem TEXT NOT NULL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Tabela AVALIACAO
CREATE TABLE avaliacao (
    id_avaliacao SERIAL PRIMARY KEY,
    nota DECIMAL(3,1) CHECK (nota >= 0 AND nota <= 10),
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    comentario TEXT,
    id_avaliador INT NOT NULL,
    id_avaliado INT NOT NULL,
    FOREIGN KEY (id_avaliador) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_avaliado) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

**Schema (resumo):**
- `usuarios(id_usuario, nome, email, senha, localizacao, data_cadastro)`
- `trocas(id_troca, data, status, id_usuario)` (FK → `usuarios`)
- `plantas(id_planta, nome_popular, tipo, origem, familia, descricao, imagem, id_usuario)` (FK → `usuarios`)
- `imagens(id_imagem, url_imagem, id_planta)` (FK → `plantas`)
- `mensagens(id_chat, mensagem, data_hora, id_usuario)` (FK → `usuarios`)
- `avaliacao(id_avaliacao, nota, data_hora, comentario, id_avaliador, id_avaliado)` (FKs → `usuarios`)

---

## 🔑 Autenticação (Opcional)
Escolha **um** dos métodos:

### A) Token Authentication (DRF)
- Adicione `rest_framework.authtoken` em `INSTALLED_APPS` e rode `migrate`.
- Crie endpoint para emissão de token (`/api/auth/token/`).
- Use nas requisições: `Authorization: Token SEU_TOKEN`.

### B) JWT (SimpleJWT)
- `pip install djangorestframework-simplejwt`
- Endpoints típicos:
  - `POST /api/auth/jwt/create/` — retorna `access` e `refresh`
  - `POST /api/auth/jwt/refresh/`
  - `POST /api/auth/jwt/verify/`
- Use nas requisições: `Authorization: Bearer SEU_ACCESS_TOKEN`.

> **Importante:** Em produção, **não** armazenar senhas em texto puro. Prefira `User` do Django com hashing (PBKDF2/Argon2).

---

## 🔗 Endpoints Principais
- Healthcheck: `GET /health/`
- Base DRF: `GET /api/`
- CRUDs:
  - `usuarios`: `/api/usuarios/`
  - `trocas`: `/api/trocas/`
  - `plantas`: `/api/plantas/`
  - `imagens`: `/api/imagens/`
  - `mensagens`: `/api/mensagens/`
  - `avaliacoes`: `/api/avaliacoes/`

---

## 📬 Exemplos de Requisição

### 1) Criar Usuário
```http
POST /api/usuarios/
Content-Type: application/json

{
  "nome": "Maria Silva",
  "email": "maria@example.com",
  "senha": "123456",
  "localizacao": "Camboriú, SC"
}
```
**Resposta (201):**
```json
{
  "id_usuario": 1,
  "nome": "Maria Silva",
  "email": "maria@example.com",
  "localizacao": "Camboriú, SC",
  "data_cadastro": "2025-12-03"
}
```

### 2) Listar Plantas
```http
GET /api/plantas/?page=1
```
**Resposta (200):**
```json
{
  "count": 1,
  "results": [
    {
      "id_planta": 10,
      "nome_popular": "Suculenta Zebra",
      "tipo": "Suculenta",
      "origem": "África",
      "familia": "Asphodelaceae",
      "descricao": "Fácil de cuidar",
      "imagem": "https://example.com/plantas/10.jpg",
      "id_usuario": 1
    }
  ]
}
```

### 3) Solicitar Troca
```http
POST /api/trocas/
Content-Type: application/json
Authorization: Bearer SEU_TOKEN

{
  "data": "2025-12-03",
  "status": "Pendente",
  "id_usuario": 1
}
```

### 4) Enviar Mensagem
```http
POST /api/mensagens/
Content-Type: application/json
Authorization: Bearer SEU_TOKEN

{
  "mensagem": "Olá! Tenho mudas disponíveis.",
  "id_usuario": 1
}
> Observação: O campo `senha` em `usuarios` não usa hashing (conforme seu esquema original). Em produção, recomendo usar autenticação do Django ou armazenar hash.

---

## 🧪 Testes com Postman
Este projeto inclui uma coleção do **Postman** para testar os endpoints da API.

### Como usar:
1. Abra o Postman.
2. Importe a coleção localizada em:
   ```
   /postman/crescer_juntos.postman_collection.json
   ```
3. Configure as variáveis de ambiente no Postman:
   - `base_url`: http://localhost:8000
   - `token`: (se necessário para autenticação)

### Endpoints na coleção:
- `GET /health/`
- `GET /api/`
- CRUDs: `/api/usuarios/`, `/api/trocas/`, `/api/plantas/`, `/api/imagens/`, `/api/mensagens/`, `/api/avaliacoes/`

---

## 🔐 Variáveis de ambiente principais
Veja `.env.example`.
- `DJANGO_SECRET_KEY` (obrigatório em produção)
- `DJANGO_DEBUG` ("1" ou "0")
- `ALLOWED_HOSTS` (separados por vírgula)
- `CORS_ALLOWED_ORIGINS` (separados por vírgula)
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`

---


## 📄 Documentação
- Diagramas e modelos estão na pasta `docs/`.
- Coleção do Postman disponível em `postman/`.

---

## 🐳 **Setup com Docker Compose e Gunicorn**

Este projeto está preparado para rodar em containers usando **Docker Compose**, com suporte a **Gunicorn** para produção e um script que aguarda o banco de dados PostgreSQL estar pronto antes de iniciar o Django.

### ✅ **Arquivos importantes**
- **Dockerfile**: Configura a imagem do Django com Gunicorn.
- **docker-compose.yml**: Orquestra os serviços `web` (Django) e `db` (PostgreSQL).
- **scripts/wait_for_db.py**: Script que aguarda o banco estar disponível antes de rodar migrações e iniciar o servidor.

### ✅ **Estrutura do Dockerfile**
```dockerfile
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends     gcc     libpq-dev     && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8000
CMD ["gunicorn", "crescer_juntos.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
```

### ✅ **Estrutura do docker-compose.yml**
```yaml
version: '3.9'
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: ${POSTGRES_DB:-crescer_juntos}
      POSTGRES_USER: ${POSTGRES_USER:-seu usuario}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-sua senha}
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  web:
    build: .
    command: bash -c "python scripts/wait_for_db.py && python manage.py migrate && gunicorn crescer_juntos.wsgi:application --bind 0.0.0.0:8000 --workers 3"
    env_file: .env
    environment:
      POSTGRES_HOST: db
    ports:
      - "8000:8000"
    depends_on:
      - db

volumes:
  pgdata:
```

### 5) Avaliar Usuário
```http
POST /api/avaliacoes/
Content-Type: application/json
Authorization: Bearer SEU_TOKEN
{
  "nota": 9.5,
  "comentario": "Ótima troca, super pontual!",
  "id_avaliador": 1,
  "id_avaliado": 2
}
```

---

## 🧪 Testes
**Rodar testes:**
```bash
pytest
```

**Com cobertura:**
```bash
coverage run -m pytest
coverage report
coverage html
```

**Dicas:**
- Use `pytest-django` e fixtures para banco.
- `pytest.ini` exemplo:
```ini
[pytest]
addopts = -ra -q
DJANGO_SETTINGS_MODULE = crescer_juntos.settings
```

---

## 📚 Documentação (Swagger/Redoc)
Com `drf-spectacular` (sugestão):
```bash
pip install drf-spectacular
```
URLs comuns:
- Swagger UI: `/api/schema/swagger-ui/`
- Redoc: `/api/schema/redoc/`
- Esquema OpenAPI (JSON): `/api/schema/`

> Alternativa: `drf-yasg` com `/swagger/` e `/redoc/`.

---

## 🔒 Boas Práticas & Segurança
- ⚠️ **Senhas**: não usar texto puro. Prefira `User` do Django com hashing (PBKDF2/Argon2).
- 🔑 **SECRET_KEY**: não commitar; usar `.env` e secret manager em produção.
- 🌍 **CORS**: restringir origens confiáveis.
- 🧱 **ALLOWED_HOSTS**: configurar domínios válidos.
- 🔐 **Auth**: preferir **JWT** para SPAs e mobile; **Token** para cenários simples.
- 🗄️ **Migrations**: sempre versionadas; não commitar banco real.
- 🧯 **Observabilidade**: endpoint `/health/` e logs estruturados.

---

## 🚀 Deploy
- **Render.com** — configurar serviço web com Docker e variáveis de ambiente.
- Banco **PostgreSQL gerenciado** (Render, Railway, Azure, Supabase).
- Use **Gunicorn** e `DEBUG=0` em produção.
- Configure **staticfiles** (ex.: `whitenoise`) se servir estáticos.

---

## 🧩 Postman
Coleção disponível em:
```
postman/crescer_juntos.postman_collection.json
```
Variáveis de ambiente:
- `base_url`: http://localhost:8000
- `token`: Bearer [seu_token]

---

## 🤝 Contribuição
1. Faça um fork.
2. Crie uma branch: `feat/minha-feature`.
3. Commit: `git commit -m "feat: minha feature"`.
4. Abra um PR descrevendo mudanças e testes.

> Sugestão: use **pre-commit** com linters (black, isort, flake8).

---

## 🧾 Licença
Este projeto está licenciado sob a **MIT License**. Crie um arquivo `LICENSE` com o texto da licença.

---

## ✒️ Autoria
**Damaris Elisangela Moreira**

---

### 🔧 Extras (opcional)
- **Makefile** com atalhos:
```makefile
run:
\tpython manage.py runserver
migrate:
\tpython manage.py migrate
test:
\tpytest
docker-up:
\tdocker-compose up --build
```
- **Seeds**: `scripts/seed.py` com dados de exemplo.
- **CI**: GitHub Actions rodando `pytest` a cada push.

---

### ✅ Pronto para Commit
```bash
git add README.md
git commit -m "docs: adiciona README profissional do projeto Crescer Juntos"
git push origin main
```

## ✅ Testes automatizados
```bash
pytest

---

## 📄 Documentação

- Diagramas e modelos estão na pasta `docs/`:
  - `diagrama_conceitual.png` → diagrama conceitual
  - `modelo_logico.png` → Modelo lógico
  - `estrutura_banco.sql` → Script SQL do banco


## 📌 Observações
- Projeto segue arquitetura limpa.
- Configuração pronta para deploy com Docker.

✒️ Autor Damaris Elisangela Moreira