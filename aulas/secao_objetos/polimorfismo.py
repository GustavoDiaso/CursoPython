# Polimorfismo em Python Orientado a Objetos

# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.

# Aplicação

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def fazer_barulho(self):
        pass


class Cachorro(Animal):
    def fazer_barulho(self):
        print("AUAUAU")


class Gato(Animal):
    def fazer_barulho(self):
        print("MIAU MIAU")


"""
Aqui temos um caso claro de polimorfismo:

Ambas as classes Gato e Cachorro possuem o mesmo método 'fazer barulho', porém,
esse método se comporta de forma diferente em cada uma delas.
"""
