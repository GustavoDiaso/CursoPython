"""
Set é uma coleção não-ordenada de valores ÚNICOS usada para armazenar múltiplos itens em um objeto, não havendo repetição de objetos. 
ão escritos com chaves ({}).

Características:
- armazena itens não duplicados 
- suporta operações matemáticas sobre conjuntos (união, instersecção)
- Não é possível modificar os ítens já existentes 
- Armazena elementos de qualquer tipo, não-ordenados e não-indexados.
"""

planetas = {'Terra', 'Marte', 'Mercúrio'}

print(planetas)

print(len(planetas))

planetas.add('Terra')
# Note que "Terra" não pode ser adicionado duas vezes
print(planetas)

try:
    print(planetas[1])

except:
    print('Os elementos dentro do Set não possuem indexes')



for i in planetas:
    print(i)


# Trasnformando array em set

array = [1,1,1,2,2,3,3,3,4,4,5,6]

arraySet = set(array)

print(arraySet)

# Como o set é uma coleção de objetos não repetidos, quando convertemos um array em um set, os elementos repetidos são eliminados