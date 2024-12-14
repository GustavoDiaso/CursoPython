"""
A função filter() em Python é uma ferramenta poderosa para filtrar elementos de uma sequência (como listas, tuplas ou outros iteráveis) 
com base em uma determinada condição. Ela é especialmente útil quando você precisa criar uma nova sequência contendo apenas os elementos 
que satisfazem um critério específico.

Como funciona:

Função de filtragem: Você fornece uma função que recebe um elemento da sequência e retorna True se o elemento deve ser incluído na nova 
sequência, ou False caso contrário.

Sequência: A função filter() também recebe a sequência que você deseja filtrar.

Iterador: A função filter() retorna um iterador que produz os elementos da sequência original que passaram no filtro.

Sintaxe:

filter(function, iterable)

"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

maiores_que_5 = list(filter(lambda numero: numero > 5, numeros))

print(maiores_que_5)

print('--------------------------')

pessoas = [
    {'nome': 'Ana Clara', 'idade': 25},
    {'nome': 'Pedro Henrique', 'idade': 30},
    {'nome': 'Maria Eduarda', 'idade': 17},
    {'nome': 'João Victor', 'idade': 35},
    {'nome': 'Laura Sofia', 'idade': 22},
    {'nome': 'Rafael Guilherme', 'idade': 28},
    {'nome': 'Beatriz Olivia', 'idade': 21},
    {'nome': 'Gabriel Lucas', 'idade': 33},
    {'nome': 'Amanda Isabelle', 'idade': 10},
    {'nome': 'Bruno Eduardo', 'idade': 32},
    {'nome': 'Isabela Alice', 'idade': 8},
    {'nome': 'Nicolas Matheus', 'idade': 29},
    {'nome': 'Sophia Helena', 'idade': 3},
    {'nome': 'Arthur Miguel', 'idade': 12},
    {'nome': 'Juliana Vitória', 'idade': 26},
    {'nome': 'Felipe Fernando', 'idade': 4},
    {'nome': 'Manuela Caroline', 'idade': 20},
    {'nome': 'Rodrigo Bernardo', 'idade': 36},
    {'nome': 'Camila Yasmin', 'idade': 7},
    {'nome': 'Daniel Davi', 'idade': 30},
]

menores_de_idade = list(filter(lambda pessoa: pessoa['idade'] <= 18, pessoas))

for pessoa in menores_de_idade:
    print(pessoa['nome'], pessoa['idade'])