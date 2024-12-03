"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


def verify_cpf_firstdigit(cpf: str) -> int:
    cpf = cpf.strip()

    formated_cpf = ""

    for char in cpf:
        try:
            char = int(char)
            formated_cpf += f"{char}"

        except ValueError:
            continue

    if len(formated_cpf) == 11:

        sum_of_digits = 0

        for i in range(0, 9):
            sum_of_digits += int(formated_cpf[i]) * (10 - i)

        print(sum_of_digits)

        first_digit = (sum_of_digits * 10) % 11

        return first_digit if first_digit <= 9 else 0

    else:
        raise ValueError("O valor passado não se trata de um CPF")


print(verify_cpf_firstdigit("522.786.478-06"))
