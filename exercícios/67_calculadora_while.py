def calculadora():
    POSSIVEIS_OPERACOES = ["*", "/", "//", "%", "-", "+", "**"]

    n1 = input("Digite o primeiro número: ").strip()
    operacao = input(' '.join(POSSIVEIS_OPERACOES) + ": ").strip()
    n2 = input("Digite o segundo número: ").strip()
    

    if ' ' not in operacao and operacao in POSSIVEIS_OPERACOES:
        try:
            n1 = float(n1)
            n2 = float(n2)

            match(operacao):
                case '*':
                    print('\nResultado', (n1 * n2)) 
                case '/':
                    print('\nResultado', (n1 / n2)) 
                case '//':
                    print('\nResultado', (n1 // n2)) 
                case '%':
                    print('\nResultado', (n1 % n2)) 
                case '**':
                    print('\nResultado', (n1 ** n2)) 
                case '+':
                    print('\nResultado', (n1 + n2)) 
                case '-':
                    print('\nResultado', (n1 - n2)) 
        except:
            print("\nAlgo deu errado!\n")
            calculadora()


    else:
        print("\nOperação inválida\n")
        calculadora()

    continuar = input("\nDeseja calcular outro valor? [s][n]").strip().lower()

    while continuar != 'n' and continuar != 's':
        print("\nNão entendi, poderia repetir?\n")
        continuar = input("Deseja calcular outro valor? [s][n]").strip().lower()
    
    if continuar == "s":
        calculadora()
    elif continuar == "n":
        print("\nPrograma finalizado!\n")


calculadora()