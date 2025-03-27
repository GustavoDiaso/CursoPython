import pymysql
from pathlib import Path
import os
from dotenv import load_dotenv

DOTENV_FILE_PATH = Path(__file__).parent / r".env"

# Instanciando nossas variáveis de ambiente
load_dotenv(DOTENV_FILE_PATH, override=True)

connection = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
)
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT NOT NULL AUTO_INCREMENT UNIQUE,
        nome VARCHAR(50) NOT NULL,
        idade INT NOT NULL,
        PRIMARY KEY (id)
    )
"""
)

connection.commit()

cursor.close()
connection.close()
