"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

def par_ou_impar():
    numero = input("Digite um número inteiro: ")

    while numero.isdigit() == False:
        numero = input("Isso não é um número inteiro. Tente novamente: ")

    try:
        numero = int(numero)
    except:
        print("Algo deu errado")

    print("Par" if numero % 2 == 0 else "Ímpar")

# par_ou_impar() 

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

def saudacao():
    horario = input("Que horas são? (padrão 24 hr 23:00) ")

    if ":" in horario and len(horario.strip()) == 5:
        
        hora = horario[0:2]
        minutos = horario[3:5]
        
        if hora.isdigit() and minutos.isdigit():

            hora = int(hora)
            minutos = int(minutos)

            if hora in range(0, 25) and minutos in range(0,60):

                if hora in range(0,12):
                    print("Bom dia")
                elif hora in range(12, 18):
                    print("Boa tarde")
                else:
                    print("Boa noite")

            else:
                print("O valor digitado não corresponde a uma hora real")
        else:
            print("O valor digitado não corresponde a uma hora real")
    else:
        print("O valor digitado não corresponde a uma hora real")

# saudacao()

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

def tamanho_nome():
    nome = input("Digite o seu nome: ")

    if len(nome) <= 4:
        print("Seu nome é curto")
    elif len(nome) > 4 and len(nome) <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande!")

# tamanho_nome()