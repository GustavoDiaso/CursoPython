# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm


def func_contador(contador: int, fim: int):
    if contador == fim:
        print(fim)
        print('fim')
    else:
        print(contador)
        func_contador(contador + 1, fim)
        


# func_contador(0, 10)


def menor_primo_mais_proximo(numero: int):
    if numero <= 1:
        return None
    

    divisores = 0

    for num in range(numero-1, 1, -1):
        if numero % num == 0:
            divisores += 1

    
    if divisores > 0:
        return(menor_primo_mais_proximo(numero-1))
    else:
        return numero


print(menor_primo_mais_proximo(6))
        
    
