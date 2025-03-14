import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "bd.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
"""
Após estabelecida a conexão com nosso banco de dados, criaremos um objeto cursor.
O cursor é um objeto que funciona como um intermediador entre o código python e o banco de dados, 
possibilitando a execução de queries SQL.
"""
cursor = connection.cursor()


cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME}
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL
    )

"""
)

# limpa a tabela inteira
cursor.execute(
    f"""
    DELETE FROM {TABLE_NAME}
    """
)

# Reindexa as linhas de forma crescente
cursor.execute(
    f"""
    DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"
    """
)

"""
O commit no sqlite tem o mesmo papel do commit no GIT:
Ele identifica as alterações feitas no banco de dados pelo cursor e aplica todas elas à versão atual 
do banco de dados.
"""
connection.commit()

cursor.execute(
    f"""
    INSERT INTO {TABLE_NAME} (name, weight)
    SELECT 'Gustavo Henrique', 70
    WHERE NOT EXISTS (
        SELECT 1 FROM {TABLE_NAME}
        WHERE name = 'Gustavo Henrique'
        AND weight = 70
    );
    """
)
connection.commit()

# Vamos reescrever o comando acima de forma a evitar SQL injections
query = f"""
    INSERT INTO {TABLE_NAME} (name, weight)
    SELECT ?, ?
    WHERE NOT EXISTS (
        SELECT 1 FROM {TABLE_NAME}
        WHERE name = ?
        AND weight = ?
    );
    """

# considere as informações abaixo como oriundas de um input válido feito pelo usuário
name = "Isabela"
weight = 70
cursor.execute(query, [name, weight, name, weight])
cursor.executemany(query, [("Paulo", 40, "Paulo", 40), ("Ronald", 80, "Ronald", 80)])

connection.commit()


cursor.close()
connection.close()
