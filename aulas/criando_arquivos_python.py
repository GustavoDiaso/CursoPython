# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
import os

caminho_arquivo = (
    "C:\\Users\\Gustavo\\Documents\\GitHub\\CursoPython\\aulas\\arquivo_para_editar\\"
)

caminho_arquivo += "arquivo.txt"

# arquivo = open(caminho_arquivo, "w")

# arquivo.close()


# ! O modo 'w' apaga tudo o que havia no arquivo previamente para que você possa sobrescrevê-lo.
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:

    arquivo.write("Nome: Gustavo Henrique\n")
    arquivo.write("Idade: 20 anos\n")

    arquivo.writelines((("Peso: 72 kg\n"), ("Irmãos: 1")))

    # print("O arquivo será fechado agora")

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:

    print(arquivo.read())

    # print("O arquivo será fechado agora")


# os.remove(caminho_arquivo) -> apaga arquivo
# os.rename(caminho_arquivo, novo_caminho_arquivo)
