"""
O parâmetro key em funções de ordenação como sort() (método de listas) e 
sorted() (função built-in) em Python é uma ferramenta poderosa que permite 
customizar a forma como os elementos de uma lista são ordenados.

O que ele faz?

Em vez de ordenar os elementos diretamente, o parâmetro key especifica uma 
função que será aplicada a cada elemento antes da comparação. O resultado 
dessa função (chamado de "chave") é então usado para determinar a ordem de 
classificação.


Por que usar o parâmetro key?

Ordenação personalizada: Permite ordenar listas com base em critérios específicos,
como o comprimento de strings, o valor de um atributo de objetos, etc.


Como funciona?

Key: O parâmetro key recebe uma função de 1 argumento, que será aplicada a cada um 
dos elementos do iterável em questão. O retorno da função é salvo de forma a atrelar 
o resultado ao elemento responsável por tal retorno.

Ordenação: A lista de retornos é ordenada de forma simples, de modo a gerar uma nova
ordenação para os elementos originais.

"""

"""
EX:

def retorna_segunda_letra(palavra):
    return palavra[1]

['Gustavo', 'Isabela', 'Pedro'].sort(key=retorna_segunda_letra)


O que ocorre dentro do sort? :

-> após aplicarmos a função retorna_segunda_letra a cada um dos elementos,
teremos algo parecido com isso:

lista_retornos = [('u', 'Gustavo'), ('s', 'Isabela'), ('e', 'Pedro')]


lista_retornos_organizada = [('e', 'Pedro'), ('s', 'Isabela'), ('u', 'Gustavo')]

-> Observe que, organizando a lista de retornos de forma simples, obtivemos
os elementos originais listados com base na segunda letra de seus respectivos nomes.

-> Agora é só retornar os elementos originais com base na organização passada.

return ['Pedro', 'Isabela', 'Gustavo']


!!! Se não tivéssemos passado uma função para key, os elementos teriam sido organizados 
com base na primeira letra do alfabeto. Como isso não ocorreu, os elementos foram 
organizados com base na lista de valores obtidos através da aplicação de uma função "X"
neles mesmos.

"""


def segunda_letra(palavra: str):
    return palavra[1]


lista = ["Gustavo", "Isabela", "Pedro"]
lista.sort(key=segunda_letra)
print(lista)
