# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def criar_multiplicador(multiplicador: int):

    def multiplicacao(numero):
        return numero * multiplicador

    return multiplicacao


multiplica_x2 = criar_multiplicador(2)
multiplica_x3 = criar_multiplicador(3)
multiplica_x4 = criar_multiplicador(4)


print(multiplica_x2(2))
print(multiplica_x3(2))
print(multiplica_x4(2))
