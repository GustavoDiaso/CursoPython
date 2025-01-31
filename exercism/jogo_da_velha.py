class JogoDaVelha():
    def __init__(self):
        self.tabuleiro = [
            [None,None,None],
            [None,None,None],
            [None,None,None],
        ]

    def verifica_vitoria(self):
        def verifica_vitoria_linha(tabuleiro_):
            "verifica se algum jogador ganhou nas linhas"
            for linha in tabuleiro_:
                if all([elemento == 'O' for elemento in linha]):
                    return 'O'
                elif all([elemento == 'X' for elemento in linha]):
                    return 'X'


        def verifica_vitoria_coluna(tabuleiro_):
            "verifica se algum jogador ganhou nas colunas"
            for indice_col in range(0, 3):
                if all(
                        [
                            tabuleiro_[0][indice_col] == 'O',
                            tabuleiro_[1][indice_col] == 'O',
                            tabuleiro_[2][indice_col] == 'O',
                        ]
                ):
                    return 'O'
                elif all(
                        [
                            tabuleiro_[0][indice_col] == 'X',
                            tabuleiro_[1][indice_col] == 'X',
                            tabuleiro_[2][indice_col] == 'X',
                        ]
                ):
                    return 'X'


        def verifica_vitoria_diagonal(tabuleiro_):
            "verifica se algum jogador ganhou nas diagonais"
            # verificando diagonal simples
            diagonal_simples = []
            for i in range(3):
                diagonal_simples.append(tabuleiro_[i][i])

            if all([jogada == 'X' for jogada in diagonal_simples]):
                return 'X'
            elif all([jogada == 'O' for jogada in diagonal_simples]):
                return 'O'

            #verificando diagonal inversa
            diagonal_inversa = []
            for i in range(3):
                j = 3 - 1 - i
                diagonal_inversa.append(tabuleiro_[i][j])

            if all([jogada == 'X' for jogada in diagonal_inversa]):
                return 'X'
            elif all([jogada == 'O' for jogada in diagonal_inversa]):
                return 'O'


        # Faz uma análise para ver se houve vitória em ulguma linha, coluna ou diagonal
        analise_vencedor = [
            verifica_vitoria_linha(self.tabuleiro),
            verifica_vitoria_coluna(self.tabuleiro),
            verifica_vitoria_diagonal(self.tabuleiro)
        ]

        # se houve vitória...
        for analise in analise_vencedor:
            if analise is not None:
                return f"{analise} venceu."

        # Se não houve vitória...
        if all([analise is None for analise in analise_vencedor]):
            # verifica se houve empate
            empate = True
            for linha in self.tabuleiro:
                for elemento in linha:
                    if elemento is None:
                        empate = False

            # se houve empate
            if empate is True:
                return 'Empate'
            # Se ninguém ganhou e não houve empate, então o jogo ainda não acabou
            else:
                return 'Em progresso'

    def jogada(self, jogador:str, coordenadas_jogada:list[int]):
        jogador = jogador.strip().upper()
        cord_x = coordenadas_jogada[0]
        cord_y = coordenadas_jogada[1]

        # verifica se o jogador foi inserido corretamente
        if jogador != 'X' and jogador != 'O':
            raise Exception("Jogador inválido! Valores aceitos: X e O")

        try:
            if self.tabuleiro[cord_x][cord_y] is None:
                self.tabuleiro[cord_x][cord_y] = jogador
            else:
                raise Exception("Essa posição está ocupada por outro jogador!")


        except IndexError:
            raise Exception("Essa posição não existe!")


    def __repr__(self):
        tabuleiro = self.tabuleiro

        def none_to_blank(elem):
            if elem is not None:
                return elem
            else:
                return ''

        linha_1 = [none_to_blank(e_) for e_ in tabuleiro[0]]
        linha_2 = [none_to_blank(e_) for e_ in tabuleiro[1]]
        linha_3 = [none_to_blank(e_) for e_ in tabuleiro[2]]

        rpr1 = f"{linha_1[0]} | {linha_1[1]} | {linha_1[2]}"
        rpr2 = f"{linha_2[0]} | {linha_2[1]} | {linha_2[2]}"
        rpr3 = f"{linha_3[0]} | {linha_3[1]} | {linha_3[2]}"

        rpr = f"""
        {rpr1}
        {'_'*max(len(rpr1), len(rpr3), len(rpr2))}
        {rpr2}
        {'_'*max(len(rpr1), len(rpr3), len(rpr2))}
        {rpr3}
        """

        return rpr


meu_jogo = JogoDaVelha()
jogador_atual = 'X'

while True:
    estado_do_jogo = meu_jogo.verifica_vitoria()

    # Se o jogo ainda não acabou
    if estado_do_jogo == 'Em progresso':

        print(f"\nVez do {jogador_atual} jogar", end='\n\n')
        print(meu_jogo)
        print('\n')
        pos_x = input("Coordenada X: ").strip()
        pos_y = input("Coordenada Y: ").strip()

        try:
            pos_x = int(pos_x)
            pos_y = int(pos_y)
        except ValueError:
            print("Coordenadas inválidas")
            continue

        try:
            meu_jogo.jogada(jogador_atual, [pos_x, pos_y])
        except Exception as e:
            print(e)
            continue


        # Muda a vez do jogador
        if jogador_atual == 'X':
            jogador_atual = 'O'
        else:
            jogador_atual = 'X'

    # Se o jogo acabou
    else:
        # caso seja um empate...
        if estado_do_jogo == 'Empate':
            print('\nEmpatou!!!\n')
            print(meu_jogo, sep='\n')
            break

        # caso seja uma vitória
        else:
            print("\nO jogo acabou!\n")
            print(estado_do_jogo)
            print(meu_jogo, sep='\n')
            break
