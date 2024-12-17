# groupby - agrupando valores (itertools)
from itertools import  groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

nomes = ["Gustavo", "Gustavo", "Isabela", "Gustavo", "Isabela", "Pedro"]

for nome, aparicoes in groupby(nomes):
    print(nome)
    print(list(aparicoes))


# note que é preciso organizar os elementos antes de agrupá-los

print('------------------------------')

for nome, aparicoes in groupby(sorted(nomes)):
    print(nome)
    print(list(aparicoes))



# vamos fazer a mesma coisa com nosso dicionário 

# 1 passo - ordenar o dicionário pelas notas dos alunos

alunos_organizados_por_nota = sorted(alunos, key=lambda aluno: aluno['nota'])

print(*alunos_organizados_por_nota, sep= '\n')

# 2 passo - organizar o dicionário
for nota, aluno in groupby(alunos_organizados_por_nota, key=lambda aluno: aluno['nota']):
    print(nota)
    print(list(aluno))


print("----------------------")

CRIANCAS = ["Ana", "Pedro", "Maria", "João", "Carlos", "Laura", "Sofia", 
            "Lucas", "Mariana", "Rafael", "Beatriz", "Gabriel", "Juliana", 
            "Gustavo", "Amanda", "Felipe", "Fernanda", "Rodrigo", "Camila", 
            "Bruno", "Isabela", "Victor", "Thaís", "Nicole", "Renan", "Alana", 
            "André", "Letícia", "Vinicius"
            ]


criancas_ordem_alfabetica:list[str] = sorted(CRIANCAS, key=lambda nome_crianca: nome_crianca[0])

grupo_letra_criancas:groupby = groupby(criancas_ordem_alfabetica, lambda nome: nome[0])

for chave, lista_nomes in grupo_letra_criancas:
    print(chave)
    print(list(lista_nomes))