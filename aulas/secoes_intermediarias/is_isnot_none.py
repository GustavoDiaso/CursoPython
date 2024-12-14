"""
is -> The is keyword is used to test if two variables refer to the same object.

The test returns True if the two objects are the same object.

The test returns False if they are not the same object, even if the two objects are 100% equal.

"""

nome = "Gustavo"

a = nome

print(a is nome)
# "a" e "nome" fazem referência ao mesmo objeto na memória


# usos comuns do is 

numero = 12

if type(numero) is int:
    print("numero é inteiro")


nada = None

if nada is None:
    print("nada é nada")


