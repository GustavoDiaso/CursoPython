# Encapsulamento (modificadores de acesso: public, protected, private)

# Python NÃO TEM modificadores de acesso


# Mas podemos seguir as seguintes convenções:

"""
(sem underline) = public
    pode ser usado em qualquer lugar.

    pode ser acessado, modificado ou chamado diretamente em qualquer parte do código


_ (um underline) = protected
    não DEVE ser usado fora da classe ou suas subclasses.

    Só pode ser acessado, modificado ou chamado através de outros métodos, getters ou setters pertencentes
    à classe pai ou a classes filhas.

__ (dois underlines) = private
   "name mangling" (desfiguração de nomes) em Python
   _NomeClasse__nome_attr_ou_method

   só DEVE ser usado na classe em que foi
   declarado.

   Só pode ser acessado, modificado ou chamado através de métodos, getters e setters originários da própria classe.

"""
class Pai:
    def __init__(self, nome: str, rg: str, comida_favorita: str):

        # A comida favorita pode ser acessada e modificada a qualquer momento, sem restrições.
        self.comida_favorita: str = comida_favorita

        # O nome do pai é protegido, só deve ser acessado via getters e não pode ser modificado diretamente dentro
        # do código
        # Instancias de classes filhas podem ter acesso a essa propriedade
        self._nome_do_pai: str = nome

        # A propriedade rg é privada. Ela não pode ser acessada ou modificada diretamente dentro do código
        # Apenas métodos originários da classe pai são capazes de modificar e mostrar tal propriedade.
        self.__rg_do_pai = rg

