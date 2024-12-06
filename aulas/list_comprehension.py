"""
list comprehension 

-> forma rápida de se criar uma lista através de um iterável

sintaxe: 

lista = [valor for valor in iterável]
"""

multiplos_de_dois = [numero * 2 for numero in range(1, 11)]


print(multiplos_de_dois)


# podemos adicionar algumas exigênicas:

multiplos_de_dois_ate_cinco = [n * 2 for n in range(1, 11) if n <= 5]

print(multiplos_de_dois_ate_cinco)
