import json

pessoa = {
    "nome": "Ana Silva",
    "idade": 30,
    "cidade": "São Paulo",
    "profissao": "Desenvolvedora",
    "hobbies": ["ler", "correr", "cozinhar"],
}

# Passo 1 - criando um arquivo .json
caminho_arquivo = (
    "C:\\Users\\Gustavo\\Documents\\GitHub\\CursoPython\\aulas\\arquivo_para_editar\\"
)
caminho_arquivo += "pessoa.json"

with open(caminho_arquivo, "w+", encoding="utf-8") as arquivo:

    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)


# Parte 2 - lendo um arquivo .json

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:

    pessoa = json.load(arquivo)
    print(pessoa)
