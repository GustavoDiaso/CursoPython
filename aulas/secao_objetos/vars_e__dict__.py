"""
__dict__ e vars retornam um dicionário contendo as propriedades de uma instância específica

"""


class Pessoa:
    """docstring for Pessoa."""

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return "Bom dia"


gustavo = Pessoa("Gustavo", 20)

print(gustavo.__dict__)
print(vars(gustavo))
