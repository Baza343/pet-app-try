import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()



import psycopg2

with psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
) as conn:
	with conn.cursor() as cur:
    	# Создание таблицы tasks with id title description completed created_at completed_at
		cur.execute('''
        	CREATE TABLE IF NOT EXISTS tasks (
             id SERIAL PRIMARY KEY,
             title VARCHAR(255) NOT NULL,
			 description VARCHAR(255),
			 completed BOOLEAN DEFAULT FALSE,
			 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
			 completed_at TIMESTAMP NULL
        	);
    	''')
		conn.commit()

  
