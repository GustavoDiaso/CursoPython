"""
A relação de composição entre duas classes se dá quando as instâncias da classe 'A' existem apenas
se uma instância da classe B também existe.

Ex: Clientes e endereços. Só faz sentido que existam instâncias da classe endereço se tais instâncias forem
utilizadas dentro de uma instância da classe clientes

"""
class Cliente:
    def __init__(self, nome: str):
        self.nome = nome


    def define_endereco(self, local:str):
        self.endereco = Endereco(local)



class Endereco:
    def __init__(self, localizacao):
        self.localizacao = localizacao



cliente1 = Cliente('Gustavo')
cliente1.define_endereco('Rua Dr. José Ória')

print(cliente1.nome, cliente1.endereco.localizacao)

"""
Nesse código específico, as instâncias de 'Endereço' servem unicamente dentro da propriedade endereço das instâncias
de clientes.
"""