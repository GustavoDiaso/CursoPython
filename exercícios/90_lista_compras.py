def lista_compras(l=None):

    if l == None:
        lista = []
    else:
        lista = l

    print("O que desejas fazer? ")
    print("Inserir [i], Remover [r], Sair [s], Listar [l]")
    resposta_1 = input("R: ").strip().lower()

    tentativas = 1

    while resposta_1 not in ("i", "s", "r", "l"):
        resposta_1 = input("R: ").strip().lower()

        if tentativas == 4:
            raise ValueError("Limite de tentativas excedido.")

        tentativas += 1

    match resposta_1:
        case "i":
            print("\n O que desejas inserir?")
            conteudo = input("R: ").strip()

            try:
                lista.append(conteudo)
                print("\n Elemento adicionado com sucesso!")
                lista_compras(lista)

            except ValueError:
                print("Impossível adicionar tal elemento à lista")

        case "r":
            print("\n O que desejas remover? \n")

            for i in range(0, len(lista)):
                print(f"[{str(i)}] -> {str(lista[i])}")

            indice_remocao = input("Informe o indice correspondente: ").strip()

            while True:
                try:
                    indice_remocao = int(indice_remocao)
                    if indice_remocao in range(0, len(lista)):
                        break
                    else:
                        raise ValueError

                except ValueError:
                    print("\n Índice inválido, informe o índice correto")
                    indice_remocao = input("R: ").strip()

            try:
                del lista[indice_remocao]
                print("\n Elemento removido com sucesso!")
                lista_compras(lista)

            except ValueError:
                print("Impossível remover tal elemento")

        case "l":
            print("\n")
            for i in range(0, len(lista)):
                print(f"[{str(i)}] -> {str(lista[i])}")

            lista_compras(lista)

        case "s":
            print("Finalizado")


lista_compras()
