# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = {
    "nome": "Luiz Otávio",
    "sobrenome": "Miranda",
    "idade": 18,
    "altura": 1.8,
    "endereços": [
        {"rua": "tal tal", "número": 123},
        {"rua": "outra rua", "número": 321},
    ],
}

print(pessoa["idade"])
print()

# O laço for itera sobre as chaves de um dicionário
for chave in pessoa:
    print(f"{chave}: {pessoa[chave]}")


# Verificando se uma chave existe dentro do dicionário
if pessoa.get("irmão", None) == None:
    print("Esta chave não existe")


# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

"""
copy - retorna uma cópia rasa (shallow copy)

Cópia Rasa (Shallow Copy):

. A cópia rasa cria uma nova instância do dicionário, mas os objetos internos (como listas ou outros dicionários) 
são compartilhados entre a cópia e o original. 

. Para fazer uma cópia rasa de um dicionário, você pode usar o método copy().

Cópia Profunda (Deep Copy):

. A cópia profunda cria uma nova instância do dicionário e, de forma recursiva, copia todos os objetos internos também. 
Isso é útil quando você quer modificar a cópia sem afetar o original.

. Para fazer uma cópia profunda de um dicionário, você pode usar o módulo copy e a função deepcopy().

"""

# get - obtém o valor associado a uma chave. Se a chave não existe, retorna um valor padrão.
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

print()
print(len(pessoa))

print(f"As chaves do dicionário pessoas são: {pessoa.keys()}")
print(f"Os valores do dicionário são: {pessoa.values()}")


for item in pessoa.items():
    print(item)


print()
pessoa.setdefault("irmão", None)
print("O irmão da pessoa é o", pessoa["irmão"])

pessoa["irmão"] = "José"
print("O irmão da pessoa é o", pessoa["irmão"])


# podemos modificar um dicionário ou adicionar novos valores a ele utilizando o método update
pessoa.update(nome="Gustavo Henrique de Oliveira Dias", irmão="Isabela", peso=70.0)

"""outra forma:

pessoa.update({
    'nome' = "Gustavo Henrique",
    'irmão' = "isabela", 
    'peso' = 70.0
})
"""
