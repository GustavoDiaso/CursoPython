"""
A função map em Python é uma ferramenta poderosa para aplicar uma função callback a cada elemento de um iterável 
(como listas, tuplas, etc.) e retornar um novo iterável com os retornos dessa callback.


Como funciona:

A função map pega cada elemento do iterável.
Aplica a função especificada a esse elemento.
Adiciona o resultado da aplicação da função ao novo iterável.
Retorna o novo iterável com os resultados.

"""

numeros = [1, 2, 3, 4, 5]

numeros_vezes_dois = list(map(lambda num: num * 2, numeros))

print(numeros_vezes_dois)
