# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Motor:
    def __init__(self, modelo: str):
        self.modelo = modelo


class Fabricante:
    def __init__(self, nome_fabricante: str):
        self.nome = nome_fabricante

class Carro:
    def __init__(self, nome:str, modelo_motor:str = None, nome_fabricante:str = None):
        self.nome = nome

        if modelo_motor is not None:
            self.motor = Motor(modelo_motor)

        if nome_fabricante is not None:
            self.fabricante = Fabricante(nome_fabricante)


    def define_motor(self, motor) -> None:
        """define o motor do carro"""
        self.motor = motor

    def define_fabricante(self, fabricante) -> None:
        """definie o fabricante do carro"""
        self.fabricante = fabricante



hb20 = Carro('Hyundai HB20')
motor_v8 = Motor('V8 - TURBO')
hyundai = Fabricante('Hyundai')

hb20.define_motor(motor_v8)
hb20.define_fabricante(hyundai)

print(hb20.nome, hb20.fabricante.nome, hb20.motor.modelo)



