# O módulo os para interação com o sistema
# Doc: https://docs.python.org/3/library/os.html
# O módulo `os` fornece funções para interagir com o sistema operacional.
# Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de
# arquivos e a função os.listdir() pode ser usada para listar os arquivos em um
# diretório. O método os.system() permite executar comandos do sistema
# operacional a partir do seu código Python.
# Windows 11 (PowerShell), Linux, Mac = clear
# Windows (antigo, cmd) = cls

import os

# path = "C:\\Users\\Gustavo\\Documents\\My Games"
# alternative_path = os.path.join("C:\\", "Users", "Gustavo", "Documents", "My Games")

# folder_path, folder = ["C:\\Users\\Gustavo\\Documents\\My Games", "F1 22"]


# files = os.listdir(path=path)
# files_ = os.listdir(path=alternative_path)

# my_games_files = os.listdir(os.path.join(folder_path, folder))

# print(files)
# print(files_)
# print(my_games_files)


# current_path = os.path.abspath(path=".")
# print(current_path)


# listando arquivos do curso
print("\nlistando arquivos do curso\n")

current_path = "C:\\Users\\Gustavo\\Documents\\GitHub\\CursoPython"


def look_into_folder(folder_path: str, deep_level=0):
    print(" " * deep_level, f"[{os.path.basename(folder_path)}]")

    for item in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, item)):
            look_into_folder(os.path.join(folder_path, item), deep_level + 3)

        else:
            print(" " * (deep_level + 2), item)


for item in os.listdir(current_path):
    relative_path = os.path.join(current_path, item)
    is_folder = os.path.isdir(relative_path)

    if is_folder and os.path.basename(relative_path) not in [
        "testes_aleatórios",
        "venv",
        ".git",
    ]:
        look_into_folder(relative_path)
    else:
        print(item)
