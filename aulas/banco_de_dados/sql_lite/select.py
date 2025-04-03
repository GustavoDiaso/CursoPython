from pathlib import Path
import sqlite3

ROOT_DIR = Path(__file__).parent
DB_NAME = "bd.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


def table_representation(table, column_names: list[str]):
    table = list(table)
    header = ""
    longgest_data_on_each_colum = []

    for row in table:
        if len(longgest_data_on_each_colum) == 0:
            for column_value in row:
                longgest_data_on_each_colum.append(str(column_value))

        for column_index in range(len(row)):
            if len(str(row[column_index])) > len(
                longgest_data_on_each_colum[column_index]
            ):
                longgest_data_on_each_colum[column_index] = row[column_index]

    # Building the header of the table (the place where the column names are displayed)
    for column_index in range(len(longgest_data_on_each_colum)):
        if len(column_names[column_index]) <= len(
            longgest_data_on_each_colum[column_index]
        ):
            header += "| "
            header += column_names[column_index]
            header += " " * (len(longgest_data_on_each_colum[column_index]))

        else:
            header += "| "
            header += column_names[column_index] + " " * len(column_names[column_index])

    header += "\n"
    header += "-" * len(header) + "\n"

    # Building the body of the table (the place where all the data is displayed by column)
    table_body = ""
    for row in table:
        row_display = ""
        for column_index in range(len(row)):
            row_display += "| "
            row_display += str(row[column_index])
            if len(column_names[column_index]) <= len(
                longgest_data_on_each_colum[column_index]
            ):
                row_display += " " * (
                    len(longgest_data_on_each_colum[column_index])
                    + len(column_names[column_index])
                    - len(str(row[column_index]))
                )
            else:
                row_display += " " * (
                    len(column_names[column_index]) ** 2 - len(str(row[column_index]))
                )

        row_display += "\n"
        table_body += row_display

    # Building our table representation
    table_repr = header + table_body
    # removing the backspace placed in the last row so the table doesn't seem to be
    # floating in the prompt
    table_repr = table_repr.rstrip("\n")
    print(table_repr)


user_name = "admin"
user_weight = 70

# response = cursor.execute(
#     "SELECT COUNT(name) FROM customers WHERE name=? and weight=?",
#     (user_name, user_weight),
# )
#
# for row in response:
#     print(row)
#     if row[0] > 0:
#         print('existe')



response = cursor.execute("SELECT * FROM customers")

table_representation(response, ["id", "name", "weight"])


cursor.close()
connection.close()
