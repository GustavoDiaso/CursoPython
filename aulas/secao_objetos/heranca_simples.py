"""
Herança -> objeto filho herda as propriedades e métodos nativos da classe pai

Classe Pai: Pessoa
    -> super class, parent class

Classe Filho: Cliente
    -> sub class, child class


Nesse exemplo, todas as instâncias da classe CLiente possuem métodos e propriedades da classe Pessoa. (Todo cliente
é também uma pessoa)

Todas as instâncias do python herdam as propriedades da classe built-in Object.


sintaxe:

class Pai:
class Filha(Pai)


super()
-> Em Python, a class super() é uma ferramenta poderosa quando se trabalha com herança entre classes.
Ela permite que instâncias de uma classe filha acessem métodos e atributos nativos de suas classes pai através
de um objeto especial que possui tais propriedades e métodos.

Basicamente, a chamada da class super nos retorna um objeto proxy, que possui todas as propriedades e métodos
da classe pai da classe que especificamos no primeiro argumento. Implicitamente, super() também recebe
uma referência à instancia atual como argumento de 'obj'. Isso se dá pelo fato de que o objeto proxy criado guardará
uma referência à instancia atual na propriedade obj e, toda vez que chamar um metodo interno, passará o objeto guardado
em 'ojb' para self, ao invés de passar uma referência a ele mesmo.

De forma simplificada, o objeto proxy retornado possui todos os métodos e propriedades da classe pai. Toda vez que
chamarmos um metodo desse objeto proxy, o objeto passado para self será nossa própria instância atual.

"""

class Pessoa:
    """instâncias de pessoa"""
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def falar(self, frase:str):
        print(frase)

class Cliente(Pessoa):
    """instâncias de clientes, que também são pessoas"""
    def __init__(self, nome: str, idade: int, endereco: str, ):
        """
        Nesse caso, o objeto proxy retornado possuirá os métodos e propriedades de classe Pessoa.
        Além disso, passaremos nossa istância atual de cliente para a propriedade obj do objeto proxy.
        Sendo assim, toda vez que proxy chamar um de seus métodos, obj (nossa instância atual) será passada
        como argumento para self.

        """
        super(Cliente, self).__init__(nome, idade)
        self.endereco = endereco


cliente1 = Cliente('Gustavo', 20, 'Rua Dr. José Ória')

print(cliente1.nome)
print(cliente1.idade)
print(cliente1.endereco)
cliente1.falar('Tudo bom, companheiro?')
