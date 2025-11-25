# Usa uma imagem leve do Python 3.12
FROM python:3.12-slim

# Evita criação de arquivos .pyc e garante logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala dependências do sistema necessárias (gcc e libpq-dev são para o PostgreSQL)
# A barra invertida (\) é essencial para quebrar a linha no comando RUN
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto
COPY . /app

# Expõe a porta 8000
EXPOSE 8000

# Inicia o servidor usando Gunicorn (Servidor de Produção)
CMD ["gunicorn", "crescer_juntos.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]