"""
A função reduce em Python é utilizada para reduzir um iterável, como uma lista, a um único valor. 
Ela aplica uma operação em todos os elementos da lista, de acordo com uma função de dois parâmetros, 
até chegar a um único resultado

Como funciona:

1 - Função redutora: Você fornece uma função que recebe dois argumentos, sendo o primeiro um acumulador e o segundo o elemento que estamos
iterando. Essa função deve retornar um único valor, que será passado para o parâmetro acumulador na próxima execução da função. 

2 - Sequência: A função reduce() também recebe a sequência que você deseja reduzir.

3 - Valor inicial: valor que será passado para o parâmetro acumulador na primeira execução da função redutora. A partir da segunda 
iteração, o valor passado para o parâmetro acumulador sera o retorno da própria função.


"""
import functools

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# forma 1 

total_gasto_1: int = sum([prod['preco'] for prod in produtos])
print(total_gasto_1)


# forma 2, via método reduce

def soma(acumulador: int, produto: dict):
    return acumulador + produto['preco']
    

total_gasto_via_reduce = functools.reduce(soma, produtos, 0)

print(total_gasto_via_reduce)


def valor_mais_alto(maior_valor: int, produto: dict) -> int:
    if maior_valor is None:
        return produto['preco']
    else:
        return max(maior_valor, produto['preco'])
    

prod_mais_caro = functools.reduce(valor_mais_alto, produtos, None)
print(prod_mais_caro)