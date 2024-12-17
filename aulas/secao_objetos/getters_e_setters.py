"""

@property é basicamente um getter no modo Pythônico
@property.setter é basicamente um setter no modo Pythônico

@property.setter - método para modificar um atributo
getter - método para obter um atributo

embora sejam métodos, getters são chamados com sintaxe de propriedade

"""

class Caneta:
    def __init__(self, cor: str):
        # atributos com '_' na frente do nome não devem ser recuperados ou alterados diretamente dentro do código.
        # Isso deve ser feito somente através de getters e setters (simulam atributos private e protected).
        self._cor: str = cor

    @property
    # Toda vez que alguém quiser acessar o valor de caneta.cor, esse método será executado.
    def cor(self):
        return self._cor

    @cor.setter
    # Toda vez que alguém quiser modificar caneta.cor, esse método será executado,
    def cor(self, nova_cor: str):
        self._cor = nova_cor


caneta1 = Caneta('Azul')
print(caneta1.cor)

caneta1.cor = 'Verde'

print(caneta1.cor)


