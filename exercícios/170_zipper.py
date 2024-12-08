# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def zipper(lista1: list, lista2: list) -> list:
    nova_lista = []

    for i in range(min(len(lista1), len(lista2))):
        nova_lista.append((lista1[i], lista2[i]))

    print(nova_lista)


zipper(["João", "Gustavo", "Pedro", "Marcio", "Queiroz"], [10, 20, 19, 34])


# Outra forma:

listas_juntas = list(
    zip(["João", "Gustavo", "Pedro", "Marcio", "Queiroz"], [10, 20, 19, 34])
)
print(listas_juntas)
