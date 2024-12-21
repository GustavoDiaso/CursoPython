"""
Classes abstratas em Python são como moldes ou blueprints para outras classes. 
Elas definem uma estrutura básica que deve ser replicada em todas as classes 
filhas, mas não podem ser instanciadas diretamente, ou seja, você não pode 
criar objetos a partir delas.

Classes abstratas = Abstract Base Class (ABC)


Por que usar classes abstratas?

Definir uma interface comum: Elas estabelecem um contrato entre classes, 
garantindo que todas as classes que herdam dela implementem certos métodos.

Promover o polimorfismo: Permitem que diferentes classes implementem um mesmo 
método de forma diferente, mas mantendo a mesma assinatura.

Evitar a criação de objetos incompletos: Ao definir métodos abstratos, você 
garante que as classes filhas implementem todas as funcionalidades necessárias.

"""

from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


"""
Explicando o código:

(from abc import ABC, abstractmethod) -> Importa as classes necessárias para criar 
classes abstratas.

( class FormaGeometrica(ABC): ) -> Define uma classe abstrata chamada FormaGeometrica 
que herda da classe ABC.

( @abstractmethod ) -> Decora os métodos area e perimetro, indicando que eles são 
abstratos e devem ser implementados nas classes filhas.

"""


class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class TrianguloRetamgulo(FormaGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
        self.diagonal = (self.base**2 + self.altura**2) ** 0.5

    def area(self):
        return self.base * self.altura / 2

    def perimetro(self):
        return self.base + self.altura + self.diagonal


"""
O que aconteceu aqui?

-> Criamos uma classe abstrata FormaGeometrica que define métodos-padrão os quais 
devem ser implementados dentro de TODAS as classes que herdem dela. Basicamente,
estamos dizendo que todas as classes que abstraem formas geometricas dentro do 
nosso código devem possuir tais métodos, mesmo que esses métodos sejam implementa-
dos de formas diferentes.

-> Criamos duas outras classes, Retangulo e TrianguloRetangulo que, por abstrairem 
formas geométricas, herdam da classe FormaGeometrica. A partir do instante que 
tais classes herdam de FormaGeometrica, ambas são obrigadas a implementar os 
métodos area e perimetro. Cada classe poderá implementar tais métodos de formas 
diferentes, porém a assintatura dos métodos (def area(self): e def perimetro(self))
deve estar presente em ambas as classes.

"""
