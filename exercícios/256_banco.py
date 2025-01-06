"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from abc import ABC, abstractmethod
import random


class Conta(ABC):
    @abstractmethod
    def __init__(
        self, dono_da_conta, agencia: int, num_conta: int, banco: str, limite: float = 0
    ):
        self._dono_da_conta = dono_da_conta
        self._agencia = agencia
        self._num_conta = num_conta
        self._banco = banco
        self._limite = limite
        self._saldo = 0

    @abstractmethod
    def _sacar(self, valor: float): ...

    @abstractmethod
    def _depositar(self, valor: float): ...


class SaldoIsuficiente(Exception): ...


class ContaCorrente(Conta):
    def __init__(
        self,
        dono_da_conta,
        agencia: int,
        num_conta: int,
        banco: str,
        limite: float = 2000,
    ):
        self._dono_da_conta = dono_da_conta
        self._agencia = agencia
        self._num_conta = num_conta
        self._banco = banco
        self._limite = limite
        self._saldo = 0

    def _sacar(self, valor: float):
        if self._saldo >= valor:
            self._saldo -= valor
            return valor
        else:
            raise SaldoIsuficiente(
                f"Saque Bloqueado. Saldo atual de R${self._saldo}. Tentativa de saque de R${valor}"
            )

    def _depositar(self, valor: float):
        self._saldo += valor

    def __repr__(self):
        rpr1 = f"Tipo: {self.__class__.__name__}, Banco: {self._banco},"
        rpr2 = f"Agência: {self._agencia}, N° da conta: {self._num_conta},"
        rpr3 = f"Saldo: {self._saldo}, Proprietário: {self._dono_da_conta.nome}"

        representation = rpr1 + "\n" + rpr2 + "\n" + rpr3

        return representation


class ContaPoupanca(Conta):
    def __init__(
        self,
        dono_da_conta,
        agencia: int,
        num_conta: int,
        banco: str,
        limite: float = 400,
    ):
        self._dono_da_conta = dono_da_conta
        self._agencia = agencia
        self._num_conta = num_conta
        self._banco = banco
        self._limite = limite
        self._saldo = 0

    def _sacar(self, valor: float):
        if self._saldo >= valor:
            self._saldo -= valor
            return valor
        else:
            raise SaldoIsuficiente(
                f"Saque Bloqueado. Saldo atual de R${self._saldo}. Tentativa de saque de R${valor}"
            )

    def _depositar(self, valor: float):
        self._saldo += valor

    def __repr__(self):
        rpr1 = f"Tipo: {self.__class__.__name__}, Banco: {self._banco},"
        rpr2 = f"Agência: {self._agencia}, N° da conta: {self._num_conta},"
        rpr3 = f"Saldo: {self._saldo}, Proprietário: {self._dono_da_conta.nome}"

        representation = rpr1 + "\n" + rpr2 + "\n" + rpr3

        return representation


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super(Cliente, self).__init__(nome, idade)
        self._contas_bancarias: list[ContaCorrente | ContaPoupanca] = []


class Banco:
    def __init__(self, nome: str, agencias: list[int]):
        self.nome = nome
        self.agencias = agencias
        self._clientes: None | list[Cliente] = None
        self._contas: None | list[ContaCorrente | ContaPoupanca] = None

    def criar_conta(
        self, proprietario: Cliente, tipo_da_conta: str
    ) -> ContaCorrente | ContaPoupanca:
        tipo_da_conta = tipo_da_conta.strip().lower()

        if tipo_da_conta == "poupanca":
            nova_conta = ContaPoupanca(
                dono_da_conta=proprietario,
                agencia=random.choice(self.agencias),
                num_conta=random.randint(100000, 999999),
                banco=self.nome,
            )
            proprietario._contas_bancarias.append(nova_conta)

            if self._clientes == None:
                self._clientes = []
                self._clientes.append(proprietario)
            else:
                self._clientes.append(proprietario)

            if self._contas == None:
                self._contas = []
                self._contas.append(nova_conta)
            else:
                self._contas.append(nova_conta)

        if tipo_da_conta == "corrente":
            nova_conta = ContaCorrente(
                dono_da_conta=proprietario,
                agencia=random.choice(self.agencias),
                num_conta=random.randint(100000, 999999),
                banco=self.nome,
            )
            proprietario._contas_bancarias.append(nova_conta)

            if self._clientes == None:
                self._clientes = []
                self._clientes.append(proprietario)
            else:
                self._clientes.append(proprietario)

            if self._contas == None:
                self._contas = []
                self._contas.append(nova_conta)
            else:
                self._contas.append(nova_conta)

    def sacar(self, cliente: Cliente, num_conta: int, agencia: int, valor_saque: float):
        if cliente in self._clientes:

            conta_referenciada = None

            for conta in cliente._contas_bancarias:
                if all(
                    (
                        conta in self._contas,
                        num_conta == conta._num_conta,
                        agencia == conta._agencia,
                    )
                ):
                    conta_referenciada = conta
                    break

            if conta_referenciada is not None:
                conta_referenciada._sacar(valor_saque)

    def depositar(self, num_conta: int, agencia: int, val_deposito: float):
        for conta in self._contas:
            if all((num_conta == conta._num_conta, agencia == conta._agencia)):
                conta._depositar(val_deposito)
                break

    # --------------------------------------------------------------------
    def __repr__(self):
        lista_nome_clientes = []
        nossas_contas = []

        for cliente in self._clientes:
            lista_nome_clientes.append(cliente.nome)

        for conta in self._contas:
            nossas_contas.append(
                (conta._dono_da_conta.nome, conta._agencia, conta.__class__.__name__)
            )

        return f"Banco: {self.nome}. Clientes: {lista_nome_clientes}. Contas: {nossas_contas}"


def main():
    cliente_gustavo = Cliente("Gustavo", 20)
    itau = Banco("Itaú", [120, 173])

    itau.criar_conta(cliente_gustavo, "corrente")

    print(itau)
    print("\n")
    print(cliente_gustavo._contas_bancarias[0])

    itau.depositar(
        num_conta=cliente_gustavo._contas_bancarias[0]._num_conta,
        agencia=cliente_gustavo._contas_bancarias[0]._agencia,
        val_deposito=400.00,
    )

    print("\n")
    print(cliente_gustavo._contas_bancarias[0])

    itau.sacar(
        cliente=cliente_gustavo,
        num_conta=cliente_gustavo._contas_bancarias[0]._num_conta,
        agencia=cliente_gustavo._contas_bancarias[0]._agencia,
        valor_saque=200.00,
    )

    print("\n")
    print(cliente_gustavo._contas_bancarias[0])


if __name__ == "__main__":
    main()
