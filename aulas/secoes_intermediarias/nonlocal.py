"""
A keyword 'nonlocal' permite que modifiquemos, dentro de uma função aninhada, variáveis definidas no escopo
superior.

Ex:

def contador():
    c = 0  # Variável no escopo de contador

    def incrementar():
        c += 1

    incrementar()
    print(c)


contador()

Nesse caso, o compilador do python gera um erro pois estamos tentando modificar a variável 'c' num escopo
onde ela não foi definida.


Para que isso seja possível, utilizaremos a keyword 'nonlocal'
"""


def contador():
    c = 0  # Variável no escopo de contador
    print(c)

    def incrementar():
        nonlocal c
        c += 1

    incrementar()
    print(c)


contador()
