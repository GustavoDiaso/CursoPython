# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

produtos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]

for prod in produtos:
    prod["preco"] = round(prod["preco"] + (prod["preco"] * 0.1), 2)


for prod in produtos:
    print(prod["nome"], prod["preco"])

print("-------------------")

novos_produtos = copy.deepcopy(produtos)

for prod in novos_produtos:
    print(prod["nome"], prod["preco"])

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

novos_produtos.sort(key=lambda prod: prod["nome"])

produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)

print("-------------------")
for prod in produtos_ordenados_por_nome:
    print(prod["nome"], prod["preco"])

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
print("-------------------")
prod_ordenados_preco = copy.deepcopy(produtos_ordenados_por_nome)

prod_ordenados_preco.sort(key=lambda prod: prod["preco"])

for prod in prod_ordenados_preco:
    print(prod["nome"], prod["preco"])
