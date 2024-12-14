import json
import recuperando_objetos_json as rec


def main():
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    p1 = Pessoa("Gustavo", 20)
    p2 = Pessoa("Isabela", 19)
    p3 = Pessoa("Giovane", 20)

    minhas_pessoas = [p1.__dict__, p2.__dict__, p3.__dict__]

    CAMINHO_BD_JSON = "C:\\Users\\Gustavo\\Documents\\GitHub\\CursoPython\\exercícios\\salvando_objetos_json\\bd_json.json"

    with open(CAMINHO_BD_JSON, "w", encoding="utf8") as arquivo_json:
        json.dump(minhas_pessoas, arquivo_json, ensure_ascii=False, indent=2)
        print("Objetos salvos com sucesso")

    pessoas_no_banco_de_dados = rec.recupera_objetos_json(CAMINHO_BD_JSON)

    print(*pessoas_no_banco_de_dados)


if __name__ == "__main__":
    main()
