# Python Dunder Methods __repr__ e __str__
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str


class Ponto:
    def __init__(self, x, y, z="String"):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f"{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})"


p1 = Ponto(1, 2)
p2 = Ponto(978, 876)
print(p1)
print(repr(p2))
print(f"{p2!r}")


class Quadrado:
    def __init__(self, lado: float):

        if isinstance(lado, float):
            self.lado = lado
            self.area = lado**2
        else:
            try:
                lado = float(lado)
                self.lado = lado
                self.area = lado**2
            except ValueError:
                raise ValueError("O parâmetro lado deve receber um float")

    def __lt__(self, other):
        # Só será possível comparar um quadrado com outro quadrado
        if isinstance(other, Quadrado):
            return self.area < other.area
        else:
            raise ValueError("Só é possível comparar um quadrado com outro quadrado.")

    def __le__(self, other):
        # Só será possível comparar um quadrado com outro quadrado
        if isinstance(other, Quadrado):
            return self.area <= other.area
        else:
            raise ValueError("Só é possível comparar um quadrado com outro quadrado.")

    def __gt__(self, other):
        # Só será possível comparar um quadrado com outro quadrado
        if isinstance(other, Quadrado):
            return self.area > other.area
        else:
            raise ValueError("Só é possível comparar um quadrado com outro quadrado.")

    def __ge__(self, other):
        # Só será possível comparar um quadrado com outro quadrado
        if isinstance(other, Quadrado):
            return self.area >= other.area
        else:
            raise ValueError("Só é possível comparar um quadrado com outro quadrado.")

    def __eq__(self, other):
        # Só será possível comparar um quadrado com outro quadrado
        if isinstance(other, Quadrado):
            return self.area == other.area
        else:
            raise ValueError("Só é possível comparar um quadrado com outro quadrado.")

    def __ne__(self, other):
        # Só será possível comparar um quadrado com outro quadrado
        if isinstance(other, Quadrado):
            return self.area != other.area
        else:
            raise ValueError("Só é possível comparar um quadrado com outro quadrado.")


quadrado1 = Quadrado(5)
quadrado2 = Quadrado(4)

if quadrado1 < quadrado2:
    print("Quadrado 1 é menor")
else:
    print("Quadrado 1 é maior")
