import enum

class Direcoes(enum.Enum):
    CIMA =  1
    BAIXO =  2
    DIREITA = 3


print(Direcoes.CIMA.value)

