# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.


class CarroDeCorrida:

    def __init__(self, cor: str, velocidade: str):
        self.cor = cor
        self.velocidade = velocidade

    def buzinar(self):
        print("BIBIBI")


carro_de_corrida = CarroDeCorrida("Vermelho", "340km/h")
print(carro_de_corrida.__class__)
print(carro_de_corrida.cor)

carro_de_corrida.buzinar()


