# CSV (Comma Separated Values - Valores separados por vírgulas)
# É um formato de arquivo que armazena dados em forma de tabela, onde cada
# linha representa uma linha da tabela e as colunas são separadas por vírgulas.
# Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
# plataformas, como por exemplo, para importar ou exportar dados para uma
# planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
# Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
# editor de texto ou em uma planilha eletrônica.
# Um exemplo de um arquivo CSV pode ser:
# Nome,Idade,Endereço
# Luiz Otávio,32,"Av Brasil, 21, Centro"
# João da Silva,55,"Rua 22, 44, Nova Era"
# A primeira linha do arquivo define os nomes das colunas da, enquanto as
# linhas seguintes contêm os valores das linhas, separados por vírgulas.
# Regras simples do CSV
# 1 - Separe os valores das colunas com um delimitador único (,)
# 2 - Cada registro deve estar em uma linha
# 3 - Não deixar linhas ou espaços sobrando
# 4 - Use o caractere de escape (") quando o delimitador aparecer no valor.

import csv
import os

folder_path = "C:\\Users\\gholiveira\\Documents\\GitHub\\CursoPython\\aulas\\secao_modulos\\modulo_csv\\"
csv_file_name = "bd_pessoas.CSV"

arquivo_csv_path = os.path.join(folder_path, csv_file_name)

with open(arquivo_csv_path) as arquivo_csv:
    # cs.reader -> lê o arquivo csv em formato de lista
    # cs.DictReader -> lê o arquivo csv em formato de dicionário
    reader = csv.DictReader(arquivo_csv)

    for linha in reader:
        print(linha)


novas_pessoas = [
    {'Nome': 'Arthur', 'Idade': 20},
    {'Nome': 'Mario', 'Idade': 29},
]

with open(arquivo_csv_path, 'a', encoding='UTF8') as arquivo_csv:
    escritor = csv.DictWriter(arquivo_csv, fieldnames=novas_pessoas[0].keys())

    for pessoa in novas_pessoas:
        escritor.writerow(pessoa)
