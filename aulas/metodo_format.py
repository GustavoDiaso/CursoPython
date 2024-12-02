# O método format faz basicamente a memsa coisa que as f-strings

nome = "Gustavo"
idade = 20
peso = 70.320

print("Olá, me chamo {} e tenho {} anos de idade. Atualmente peso {:.2f} kg".format(nome, idade, peso))


# forma 2

nome = 'Gu'
irma = 'Isabela'
idade = 20
pesoIrma = 66.345


print("""Olá, meu nome é {nome}. Atualmente tenho {idade} anos de idade e moro com minha irmã {nome_irma}.
Como ela é muito gorda, atualmente pesa {peso:.2f} kg...""".format(nome=nome, idade=idade, nome_irma=irma, 
peso = pesoIrma))

