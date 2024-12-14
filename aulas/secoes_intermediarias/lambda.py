"""
Em Python, funções lambda são funções anônimas (sem nome) definidas em uma única 
linha.

Elas são especialmente úteis quando você precisa de uma função simples para uma 
tarefa específica, sem a necessidade de definir uma função completa com um nome.

sintaxe:

lambda parametro: retorno
"""

lista = [1, 2, 3]

dobrar = lambda x: x * 2

for elemento in lista:
    print(dobrar(elemento))


# Muito útil para callbacks


def saudar(nome, saudacao):
    print(saudacao(nome))


saudar("Pedro", lambda nome: f"Olá, {nome}. Como vai?")


# Podemos passar funções lambda para o parâmetro key do método sort para obtermos uma organização personalizada.

lista = ["Gustavo", "Isabela", "Pedro"]

lista.sort(key=lambda palavra: palavra[1])
print(lista)


"""-------------------------------------------------------------------"""
""" Convertendo funções para lambda """

def executa_funcao(funcao, *argumentos):
    return funcao(*argumentos)


print(executa_funcao(lambda x, y: x + y, 2,3))


def cria_multiplicador(multiplicador):
    def func_multiplicar(valor):
        return valor * multiplicador
    
    return func_multiplicar


multiplica_por_tres = cria_multiplicador(3)
print(multiplica_por_tres(2))


soma = lambda *args: sum(args)

print(soma(1,2,3,4))



