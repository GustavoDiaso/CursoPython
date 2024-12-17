"""
O que são métodos de classe?

Em Python, métodos de classe são funções definidas dentro de uma classe que são
acessadas pela própria classe, e não por uma instância específica da classe.

Eles são decorados com o decorador @classmethod e o valor passado para o primeiro parâmetro do método,
no caso, cls por convenção, é a classe que chama o método em si.


Quando usar métodos de classe?

Métodos utilitários: Quando você precisa de um método que realiza uma operação relacionada à classe,
mas não depende de um estado específico de uma instância.

Métodos de fábrica: Para criar instâncias de uma classe de forma personalizada, com base em diferentes
parâmetros de entrada.

Métodos que operam em atributos de classe: Quando você precisa acessar ou modificar atributos que pertencem
à classe, e não a instâncias individuais.

"""

class Pessoa:
    def __init__(self, nome: str, idade: str):
        self.nome: str = nome
        self.idade: str = idade

    def falar(self) -> None:
        print(self.nome)

    # Criando um método cujo objetivo é retornar objetos da Classe pessoa com exatos 50 anos
    @classmethod
    def criar_com_50_anos(cls, nome: str):
        # cls é uma referência à própria classe
        return cls(nome, 50)


cinquentao = Pessoa.criar_com_50_anos('Gustavo')

print(cinquentao.idade)
cinquentao.falar()

