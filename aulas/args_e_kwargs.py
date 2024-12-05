"""
*args e **kwargs: Uma Explicação Detalhada

Em Python, *args e **kwargs são ferramentas poderosas para criar funções mais flexíveis, permitindo que você passe um 
número variável de argumentos. A principal diferença entre eles reside no tipo de argumentos que capturam:

*args
Argumentos posicionais: Captura um número arbitrário de argumentos posicionais e os coloca em uma tupla.
Ordem: A ordem dos argumentos é preservada na tupla resultante.
Uso: Ideal para quando você não sabe de antemão quantos argumentos serão passados para a função, mas eles não possuem nomes específicos.
Exemplo:

def minha_funcao(*args):
    for arg in args:
        print(arg)

minha_funcao(1, 2, 3, "olá")

*kwargs
Argumentos nomeados: Captura um número arbitrário de argumentos nomeados e os coloca em um dicionário.
Chaves e valores: As chaves do dicionário são os nomes dos argumentos e os valores são os valores correspondentes.
Uso: Ideal para quando você deseja passar argumentos adicionais à função, mas não sabe quais serão.

Exemplo:

def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

minha_funcao(nome="João", idade=30, cidade="São Paulo")


"""

def argumentos_nomeados(**kwargs):
    print(kwargs)


argumentos_nomeados(nome='Gustavo', idade=20)



"""
Em Python, o operador ** (dois asteriscos) tem um papel específico quando utilizado com dicionários: ele desempacota um dicionário.

Desempacotar um dicionário em Python significa basicamente transformar suas chaves e valores em argumentos nomeados.


Por que Desempacotar?

Simplificar o código: Torna o código mais conciso e legível, especialmente quando você precisa acessar múltiplos valores de um dicionário.
Passar argumentos para funções: Permite passar os elementos de um dicionário como argumentos nomeados para uma função.
Criar novos dicionários: Facilita a criação de novos dicionários a partir de dicionários existentes.

"""
parametros = {
    'nome': 'Gustavo',
    'idade': '20'
}

# Extraindo os valores de "parametros" na forma de argumentos nomeados e passando tais argumentos para uma nova função.
argumentos_nomeados(**parametros)