# Crescer Juntos – Backend Limpo (Django + PostgreSQL)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-4.2-green)
![License](https://img.shields.io/badge/license-MIT-green)

Este projeto é um backend desenvolvido com **Django** e banco de dados **PostgreSQL**, seguindo boas práticas de organização e escalabilidade.

---

## 📂 Estrutura do Projeto

crescer_juntos/
├── crescer_juntos/          # Configurações globais do Django (settings, urls)
├── docs/                    # Documentação e diagramas do Banco de Dados
├── main/                    # Aplicação principal (Models, Views, Serializers)
├── postman/                 # Coleções de teste da API (JSON)
├── scripts/                 # Scripts auxiliares
├── staticfiles/             # Arquivos estáticos gerados pelo Whitenoise
├── .env.example             # Modelo das variáveis de ambiente
├── .gitignore               # Arquivos ignorados pelo Git
├── docker-compose.yml       # Orquestração dos containers (App + DB)
├── Dockerfile               # Receita para criar a imagem Docker da API
├── manage.py                # Gerenciador de comandos do Django
├── pytest.ini               # Configuração dos testes automatizados
└── requirements.txt         # Lista de dependências do projeto
```
CRESCER_JUNTOS
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
├── scripts
└── docs
    ├── diagrama_conceitual.png
    ├── estrutura_banco.sql
    └── modelo_logico.png
```

---

## 🚀 Instalação e Configuração

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/xdammyx/Projeto-crescer_juntos
cd crescer_juntos
```

### 2️⃣ Crie e ative o ambiente virtual
```bash
python -m venv .venv
.\.venv\Scripts\Activate   # Windows
source .venv/bin/activate  # Linux/Mac
```

### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

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

## ▶️ Como Rodar o Projeto

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

---

## ✅ Testes
```bash
pytest
```

---

## 🔐 Variáveis de Ambiente
- `CORS_ALLOWED_ORIGINS` (separados por vírgula)
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`

---

## 📄 Documentação
- Diagramas e modelos estão na pasta `docs/`.
- Coleção do Postman disponível em `postman/`.

---

## 📌 Observações
- Projeto segue arquitetura limpa.
- Configuração pronta para deploy com Docker.
