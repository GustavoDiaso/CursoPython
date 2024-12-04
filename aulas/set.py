# Sets - Conjuntos de objetos imutáveis e únicos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {"Luiz", 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

lista = [1, 2, 3, 4, 4, 4]
lista_unica = list(set(lista))
print(lista_unica)

# Métodos úteis:
# add, update, clear, discard


# Operadores úteis:

s1 = {1, 2, 3}
s2 = {3, 4, 5}

# união | união (union) - Une
uniao = s1 | s2
print("união", uniao)

# intersecção & (intersection) - Itens presentes em ambos
intersecao = s1 & s2
print("interseção", intersecao)

# diferença - Itens presentes apenas no set da esquerda
diff = s1 - s2
print("diferença", diff)

# diferença simétrica ^ - Itens que não estão em ambos
diff_simetrica = s1 ^ s2
print("Diferença simétrica", diff_simetrica)
