from pathlib import Path
import sqlite3

ROOT_DIR = Path(__file__).parent
DB_NAME = "bd.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


def get_rows():
    response = cursor.execute(f"SELECT * FROM {TABLE_NAME}")

    for row in response:
        print(row)


get_rows()

cursor.execute(
    f"""
    UPDATE {TABLE_NAME}
    SET name = ?
    WHERE id = ?
""",
    ["administrador", 5],
)

get_rows()


cursor.close()
connection.close()
