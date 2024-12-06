def main():
    try: 
        a = 10
        b = 5
        c = a/b
    except (TypeError, IndexError):
        print("Sintaxe inexperada")

    except ZeroDivisionError:
        print("Impossível dividir por 0")

    except Exception as exceçao:
        print("Algum erro ocorreu")
        print(exceçao)
        print('Error class', exceçao.__class__.__name__)
    finally:
        # O bloco finally sempre será executado, independentemente do resultado do try except 
        print("Bom dia")


if __name__ == '__main__':
    main()



