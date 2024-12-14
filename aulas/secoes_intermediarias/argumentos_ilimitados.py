"""
É possível passar um número indeterminado de argumentos para uma função utilizando o parâmetro
*args (args por convensão)

*args receberá um numéro x de argumentos e os armazenará na forma de uma tupla.

"""


def soma(*args) -> float:
    soma = 0
    for num in args:
        soma += num

    return float(soma)


print(soma(1, 2, 3, 4))
