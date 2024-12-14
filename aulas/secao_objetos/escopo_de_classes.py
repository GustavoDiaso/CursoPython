class Animal:
    # esta propriedade será herdada por todas as instâncias da classe
    #  Animal e só poderá ser editada dentro da classe.
    planeta = "Terra"

    def __init__(self, nome):
        self.nome = nome


print(Animal.planeta)

crocodilo = Animal("Crocodilo")

print(crocodilo.nome)
print(crocodilo.planeta)
