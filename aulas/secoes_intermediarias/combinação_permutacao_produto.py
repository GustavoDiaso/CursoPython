# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
import itertools

pessoas = [
    "João",
    "Joana",
    "Luiz",
    "Letícia",
]
camisetas = [
    ["preta", "branca"],
    ["p", "m", "g"],
    ["masculino", "feminino", "unisex"],
    ["algodão", "poliéster"],
]

# print("Combinação pessoas:")
# print(*list(itertools.combinations(pessoas, 2)), sep="\n")

# print("Permutação pessoas:")
# print(*list(itertools.permutations(pessoas, 2)), sep="\n")

print(*list(itertools.product(*camisetas)), sep="\n")
