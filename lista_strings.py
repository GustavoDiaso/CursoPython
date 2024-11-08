"""
tipo list -> mutável

uma lista em python é uma coleção de elementos(objetos)


"""

# deletando um elemento dentro da list e reorganizando os índices
l1 = [10, 20, 30, 40]
del l1[1]
print(l1)

# adicionando objetos ao final da lista
l1.append(50)
print(l1)

# removendo um elemento específico dentro da lista. A diferença deste método para a
# palavra reservada del é que o método pop retorna o objeto que acabou de ser
# removido
removido = l1.pop(0)
print(l1)
print(removido)


# apagando todo o conteúdo da minha lista
# l1.clear()


# concatenando e extendendo uma lista
lista_a = [1, 2, 3, 4]
lista_b = [5, 6, 7, 8]

juncao = lista_a + lista_b
print(juncao)


lista_a2 = [1, 2, 3]
lista_b2 = [4, 5, 6]

# o método extend faz alterações no objeto que o chama
lista_a2.extend(lista_b2)
print(lista_a2)
