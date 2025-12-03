# Crescer Juntos – Backend Limpo (Django + PostgreSQL)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.12-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/django-5.0-green?style=for-the-badge&logo=django)
![PostgreSQL](https://img.shields.io/badge/postgresql-13+-blue?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/docker-ready-blue?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

Este projeto é um backend desenvolvido com **Django** e banco de dados **PostgreSQL**, seguindo boas práticas de organização e escalabilidade.

---

## 📂 Estrutura do Projeto

✅crescer_juntos/# Configurações globais do Django (settings, urls)

✅docs/# Documentação e diagramas do Banco de Dados

✅main/# Aplicação principal (Models, Views, Serializers)

✅postman/# Coleções de teste da API (JSON) scripts/# Scripts auxiliares

✅staticfiles/# Arquivos estáticos gerados pelo Whitenoise

✅.env.example# Modelo das variáveis de ambiente

✅.gitignore# Arquivos ignorados pelo Git

✅docker-compose.yml# Orquestração dos containers (App + DB)

✅Dockerfile# Receita para criar a imagem Docker da API

✅manage.py# Gerenciador de comandos do Django

✅pytest.ini# Configuração dos testes automatizados

✅requirements.txt# Lista de dependências do projeto
```
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
# ✅ Requisitos
- Python 3.12+
- PostgreSQL 13+(Obs? utilizei a versão 18)
- (Opcional) Docker e Docker Compose

---

## ⚙️ Configuração do Banco de Dados

Crie um banco PostgreSQL e configure as variáveis no arquivo `.env`:
```
POSTGRES_DB=crescer_juntos
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

---
## 🎨 Diagramas do Banco de Dados

### Conceitual
![Diagrama Conceitual](docs/diagrama_conceitual.png)

### Lógico
![Diagrama Lógico](docs/modelo_logico.png)

## 🚀 Instalação e Configuração

## ▶️ Como Rodar o Projeto ## 

🚀 Instalação rápida (sem Docker)

### Rodar migrações
```bash
python manage.py migrate
```

### Criar superusuário
```bash
python manage.py createsuperuser
```

### Rodar servidor
```bash
python manage.py runserver
```
---
## 🐳 Deploy com Docker

Este projeto possui suporte a **Docker** e **Docker Compose**.

### 1️⃣ Build e subir os containers
```bash
docker-compose up --build
```

### 2️⃣ Acessar o container
```bash
docker exec -it crescer_juntos_web bash
```

### 3️⃣ Rodar migrações dentro do container
```bash
python manage.py migrate
```

## 🔗 Endpoints principais
- Healthcheck: `GET /health/`
- API base (DRF): `GET /api/`
- CRUDs:
  - `usuarios`: `/api/usuarios/`
  - `trocas`: `/api/trocas/`
  - `plantas`: `/api/plantas/`
  - `imagens`: `/api/imagens/`
  - `mensagens`: `/api/mensagens/`
  - `avaliacoes`: `/api/avaliacoes/`

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
- ## 🔐 Variáveis de Ambiente
- `CORS_ALLOWED_ORIGINS` (separados por vírgula)
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`

---

## ✅ Testes automatizados
```bash
pytest
---

## 📄 Documentação
- Diagramas e modelos estão na pasta `docs/`.
- Coleção do Postman disponível em `postman/`.

---

## 📌 Observações
- Projeto segue arquitetura limpa.
- Configuração pronta para deploy com Docker.
