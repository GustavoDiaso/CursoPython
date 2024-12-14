"""
Closure

Closures são funções que "lembram" do escopo em que foram criadas, mesmo após esse escopo ter 
sido encerrado. 

Em Python, isso ocorre quando uma função aninhada (ou interna) mantém uma referência às 
variáveis locais do escopo da função externa, mesmo depois que a execução desta última é 
concluída.

Como funcionam as closures?
Uma função é definida dentro de outra função.
A função interna utiliza variáveis do escopo da função externa.
A função externa retorna a função interna.
As variáveis do escopo externo são preservadas na função interna.
"""


def funcao_externa(nome: str):

    def closure(saudacao: str):
        print(saudacao + nome)

    return closure


nome1 = funcao_externa("Gustavo")


nome1("Bom dia, ")
nome1("Olá, ")
