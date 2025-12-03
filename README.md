# Crescer Juntos – Backend Limpo (Django + PostgreSQL)

# 🌱 Crescer Juntos - API Backend

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-316192?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker)

> Este projeto é um backend desenvolvido com **Django** e banco de dados **PostgreSQL**, seguindo boas práticas de organização, arquitetura limpa e escalabilidade.

**Crescer Juntos** é uma API REST desenvolvida para gerenciar uma plataforma de troca de plantas e jardinagem colaborativa. O sistema conecta usuários que desejam trocar mudas, sementes e conhecimentos, promovendo a sustentabilidade.

---

## 🚀 Funcionalidades

- **👤 Gerenciamento de Usuários:** Cadastro, perfil e localização.
- **🌿 Catálogo de Plantas:** Cadastro detalhado com nome popular, científico, origem, família e fotos.
- **🔄 Sistema de Trocas:** Solicitação e gerenciamento de status (*Pendente, Aceito, Recusado*).
- **💬 Chat:** Envio de mensagens entre usuários interessados na troca.
- **⭐ Avaliações:** Sistema de notas e comentários para reputação dos usuários.
- **❤️ Health Check:** Monitoramento de status da API.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12
- **Framework:** Django 5 & Django REST Framework (DRF)
- **Banco de Dados:** PostgreSQL (Versão 13+ / Testado na 18)
- **Testes:** Pytest (Unitários/Integração) & Postman (E2E)
- **Infraestrutura:** Docker, Docker Compose
- **Servidor:** Gunicorn, Whitenoise
- **Deploy:** Render.com

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
## ⚙️ Pré-requisitos e Instalação

### Requisitos
- Python 3.12+
- PostgreSQL 13+ (Projeto desenvolvido na versão 18)
- Git
- (Opcional) Docker e Docker Compose

### 1️⃣ Clonar o repositório
```bash
git clone [https://github.com/xdammyx/Projeto-crescer_juntos](https://github.com/xdammyx/Projeto-crescer_juntos)
cd crescer_juntos
### 2️⃣ Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto baseado no exemplo:

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

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/xdammyx/Projeto-crescer_juntos
cd crescer_juntos
```

### 2️⃣ Crie e ative o ambiente virtual

- **Windows (PowerShell):**
powershell
python -m venv .venv
.\.venv\Scripts\Activate

- **Windows (CMD):**
cmd
python -m venv .venv
.\.venv\Scripts\activate.bat

- **Linux/Mac:**
bash
python -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Instale as dependências

pip install -r requirements.txt

## ▶️ Como Rodar o Projeto ## 

### Rodar migrações

python manage.py migrate
```

### Criar superusuário

python manage.py createsuperuser
```

### Rodar servidor

python manage.py runserver
```
Acesse a API em: http://127.0.0.1:8000/api/
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

✒️ Autor Damaris Elisangela Moreira
