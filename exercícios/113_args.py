# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiply_values(*values) -> float:
    """This function is capable of multiplying a large amount of numbers"""
    for element in values:
        if isinstance(element, float) or isinstance(element, int):
            continue
        else:
            raise ValueError("Um dos valores passados não é um número")

    if len(values) == 1:
        return values[0]

    else:
        multiplication = values[0]
        for number_index in range(1, len(values)):
            multiplication = multiplication * values[number_index]

        return float(multiplication)


multiplicacao = multiply_values(2.3, 2.5, 2.5, 2, 2)

print(multiplicacao)
