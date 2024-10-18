def apareceu_mais_vezes() -> None:

    string = "Testando a contagem de letras dentro de uma string".lower()

    vencedora = [0, ""]

    for letra in string:

        if letra not in " ,.;:?()!" and letra.isdigit() == False:
            qtd = string.count(letra)

            if qtd > vencedora[0]:
                vencedora[0] = qtd
                vencedora[1] = letra

    print(
        f'A letra que mais apareceu foi "{vencedora[1]}" com um total de {vencedora[0]} aparições"'
    )


apareceu_mais_vezes()
