def saudacao():
    print("Olá")


"""Você pode passar uma função para uma variável."""
func_saudacao = saudacao
"""func_saudacao referencia a função saudação na memória."""

func_saudacao()


def saudam_o_rei(saudacao):
    saudacao()


saudam_o_rei(saudacao=saudacao)
