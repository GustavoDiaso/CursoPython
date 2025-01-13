# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

import os


caminho = "C:\\Users\\gholiveira\\Documents\\GitHub\\CursoPython\\aulas\\secao_modulos"

for root, dirs, files in os.walk(caminho):
    print('\nPasta atual: ', root)
    print('Diretórios:')
    if len(dirs) != 0:
        print(*dirs, sep='\n')

    print('\nFiles:')
    if len(files) != 0:
        print(*files, sep='\n')

    print("--------------------------------")


