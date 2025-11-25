
import os
import time
import psycopg2

host = os.getenv('POSTGRES_HOST', 'localhost')
port = int(os.getenv('POSTGRES_PORT', '5432'))
db = os.getenv('POSTGRES_DB', 'crescer_juntos')
user = os.getenv('POSTGRES_USER', 'damy')
password = os.getenv('POSTGRES_PASSWORD', 'damy2109')

for i in range(60):
    try:
        conn = psycopg2.connect(host=host, port=port, dbname=db, user=user, password=password)
        conn.close()
        print('Database is ready!')
        break
    except Exception as e:
        print(f'Waiting for DB... ({i+1}/60) {e}')
        time.sleep(1)
else:
    raise RuntimeError('Database not ready after waiting 60 seconds')
