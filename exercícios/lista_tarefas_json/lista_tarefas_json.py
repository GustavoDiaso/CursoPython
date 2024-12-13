import json


def lista_tarefas() -> None:

    lista_comandos = [
        "Mostrar tarefas",
        "Adicionar_tarefa",
        "Desfazer",
        "Refazer",
        "Sair",
    ]

    tarefas = []
    tarefas_removidas = []
    caminho_json_tarefas = "C:\\Users\\Gustavo\\Documents\\GitHub\\CursoPython\\exercícios\\lista_tarefas_json\\tarefas.json"

    # Funções básicas do programa

    def mostra_tarefas(lista_tarefas: list[str]) -> None:
        print("\n")
        print(*lista_tarefas, sep="\n")
        print("\n")

    def adiciona_tarefa(tarefa: str, lista_tarefas: list[str]) -> None:
        lista_tarefas.append(tarefa)

    def desfaz_ultima_tarefa(
        lista_tarefas: list[str], lista_tarefas_removidas: list[str]
    ) -> None:
        if len(lista_tarefas) > 0:
            lista_tarefas_removidas.append(lista_tarefas.pop())
        else:
            raise ValueError("Não há tarefas para serem desfeitas")

    def restaura_ultima_tarefa_excluida(
        lista_tarefas: list[str], lista_tarefas_removidas: list[str]
    ) -> None:
        if len(lista_tarefas_removidas) > 0:
            lista_tarefas.append(lista_tarefas_removidas.pop())
        else:
            raise ValueError("Não há mais tarefas para serem refeitas")

    def autualiza_json_tarefas(
        lista_tarefas: list[str], caminho_arquivo_json: str
    ) -> None:

        with open(caminho_arquivo_json, "w", encoding="utf8") as arquivo_json:
            json.dump(lista_tarefas, arquivo_json, ensure_ascii=False, indent=2)

    #####################################################

    while True:

        for codigo_tarefa, tarefa in enumerate(lista_comandos):
            print(f"[{codigo_tarefa}] {tarefa}")

        comando = input("O que desejas fazer? ").strip()

        # Verificando se o código digitado é valido
        while True:
            try:
                comando = int(comando)

                if comando not in range(len(lista_comandos)):
                    raise ValueError("Código de tarefa inválido ")
                else:
                    break

            except ValueError:
                comando = input("Código Inválido. O que desejas fazer? ").strip()

        # Executando as ações com base no comando do usuário:
        match comando:
            case 0:
                mostra_tarefas(tarefas)
            case 1:
                tarefa = input("Qual tarefa deseja realizar? ").strip()
                adiciona_tarefa(tarefa, tarefas)

                autualiza_json_tarefas(
                    tarefas, caminho_arquivo_json=caminho_json_tarefas
                )

            case 2:
                try:
                    desfaz_ultima_tarefa(tarefas, tarefas_removidas)

                    autualiza_json_tarefas(
                        tarefas, caminho_arquivo_json=caminho_json_tarefas
                    )
                except ValueError:
                    print("Não há tarefas para serem desfeitas")

            case 3:
                try:
                    restaura_ultima_tarefa_excluida(tarefas, tarefas_removidas)

                    autualiza_json_tarefas(
                        tarefas, caminho_arquivo_json=caminho_json_tarefas
                    )
                except ValueError:
                    print("Não há mais tarefas para serem refeitas")
            case 4:
                break


lista_tarefas()
