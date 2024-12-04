"""
Dada uma lista de elementos, retorne o primeiro elemento a ser visto duas vezes, considerando a ordem
de aparição da esquerda para a direita.

Caso não haja elementos repetidos, retorne -1
 """

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def first_duplicate(list_: list):
    seen_elements = set()

    for element in list_:
        if element in seen_elements:
            return element
        else:
            seen_elements.add(element)

    return -1


for lista_index in range(0, len(lista_de_listas_de_inteiros)):
    print(
        "lista",
        lista_index + 1,
        ":",
        first_duplicate(lista_de_listas_de_inteiros[lista_index]),
    )
