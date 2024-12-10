"""
O operador Warlus (morsa) ':=' funciona praticamente da mesma maneira que o operador '='. A única diferença é que o operador warlus retorna 
o conteúdo da variável após atribuí-la a um objeto na memória. 

"""

clientes =  {
    0: 'Gustavo',
    1: 'Isabela',
    2: 'Pedro',
    3: 'Arthur'
}


if cliente := clientes.get(2):
    print(f"Bom dia, {cliente}. Como vai?")
else:
    print("Cliente não encontrado no banco de dados")


# Note que a variável cliente continua a existir no escopo global, mesmo que ela tenha sido definida numa expressão if.
print(cliente)