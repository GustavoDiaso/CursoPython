# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


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
                print("\n")
                print(*tarefas, sep="\n")
                print("\n")
            case 1:
                tarefa = input("Qual tarefa deseja realizar? ").strip()
                tarefas.append(tarefa)

            case 2:
                if len(tarefas) > 0:
                    tarefas_removidas.append(tarefas.pop())
                else:
                    print("Não há tarefas para serem desfeitas")

            case 3:
                if len(tarefas_removidas) > 0:
                    tarefas.append(tarefas_removidas.pop())
                else:
                    print("Não há nada para ser refeito")

            case 4:
                break


lista_tarefas()
