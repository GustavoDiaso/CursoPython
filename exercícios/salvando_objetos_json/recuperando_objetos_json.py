import json


def recupera_objetos_json(caminho_json):
    with open(caminho_json, "r", encoding="utf8") as arquivo_json:
        return json.load(arquivo_json)
