"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


def jogo_palavra_secreta():
    palavra_secreta = "CHIPANZÉ"
    contador_tentativas = 1
    palavra_mascarada = "*" * len(palavra_secreta)
    letras_erradas = ""

    while palavra_mascarada != palavra_secreta:
        tentativa = input("Digite uma letra qualquer: ").upper().strip()

        if (
            tentativa.isdigit() == False
            and len(tentativa) == 1
            and tentativa not in " ,.;:?()!"
        ):

            mascara_atual = ""

            for i in range(0, len(palavra_secreta)):

                if palavra_mascarada[i] != "*":
                    mascara_atual += palavra_mascarada[i]

                else:
                    if tentativa == palavra_secreta[i]:
                        mascara_atual += tentativa

                    else:
                        mascara_atual += "*"
                        letras_erradas += tentativa + " "

            palavra_mascarada = mascara_atual

            print("\n", palavra_mascarada)
            print(f"\n Você está na tentativa {contador_tentativas}")

            contador_tentativas += 1

    print("\nParabéns, você venceu")


jogo_palavra_secreta()
