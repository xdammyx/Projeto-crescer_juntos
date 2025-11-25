
# Backend limpo — projeto **crescer_juntos** (Django + PostgreSQL)

Este backend foi refeito do zero, limpo e pronto para rodar, usando Django 5, DRF e CORS.
- **Projeto Django**: `crescer_juntos`
- **App**: `main` (na pasta `main/`)
- **Banco**: `crescer_juntos` (PostgreSQL)
- **Usuário**: `damy` | **Senha**: `damy2109`

## Requisitos
- Python 3.12+
- PostgreSQL 13+
- (Opcional) Docker e Docker Compose

## Configuração rápida (sem Docker)
1. Crie e ative o virtualenv:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   ```
2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Crie `.env` a partir do exemplo:
   ```bash
   cp .env.example .env
   ```
4. Aplique migrações:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Crie um superusuário (opcional):
   ```bash
   python manage.py createsuperuser
   ```
6. Suba o servidor de desenvolvimento:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

### Endpoints
a) Healthcheck de banco: `GET /health/`  
b) API base (DRF): `GET /api/` (lista de rotas)  
c) CRUDs:
- `usuarios`: `/api/usuarios/`
- `trocas`: `/api/trocas/`
- `plantas`: `/api/plantas/`
- `imagens`: `/api/imagens/`
- `mensagens`: `/api/mensagens/`
- `avaliacao`: `/api/avaliacoes/`

> Observação: O campo `senha` em `usuarios` não usa hashing (conforme seu esquema original). Em produção, recomendo usar autenticação do Django ou armazenar hash. 

## Rodando com Docker
1. Ajuste o `.env` (ou use `.env.example`).
2. Suba os serviços:
   ```bash
   docker compose up --build
   ```
   - App: http://localhost:8000
   - Postgres: porta 5432 exposta localmente

## Variáveis de ambiente principais
Veja `.env.example`.
- `DJANGO_SECRET_KEY` (obrigatório em produção)
- `DJANGO_DEBUG` ("1" ou "0")
- `ALLOWED_HOSTS` (separados por vírgula)
- `CORS_ALLOWED_ORIGINS` (separados por vírgula)
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`

## Estrutura
```
crescer_juntos_backend/
├─ creser_juntos/        # projeto Django (settings/urls)
│  ├─ settings.py, urls.py, asgi.py, wsgi.py
├─ main/                 # app principal
│  ├─ models.py, serializers.py, views.py, urls.py, admin.py
│  └─ migrations/__init__.py
├─ scripts/wait_for_db.py
├─ manage.py
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ pytest.ini
└─ .env.example
```
