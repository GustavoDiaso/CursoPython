class A(object):
    def __init__(self, a):
        self.atributo_a = a


class B(A):
    def __init__(self, b, a):
        self.atributo_b = b
        super(B, self).__init__(a)


class C(B):
    def __init__(self, c, b, a):
        self.atributo_c = c
        super(C, self).__init__(b, a)


c = C("c", "b", "a")

print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
