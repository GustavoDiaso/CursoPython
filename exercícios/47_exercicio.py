nome_usuario = input("Qual é o seu nome? ")
idade_usuario = input("Quantos anos você tem? ")

if len(nome_usuario) and len(idade_usuario) != 0:
    while True:
        try:
            idade_usuario = int(idade_usuario)
            break
        except:
            print("Você não digitou a idade corretamente")
            idade_usuario = input("Quantos anos você tem? ")


    espacos = "Seu nome não contém espaços"
    
    if ' ' in nome_usuario:
        espacos = "Seu nome contém espaços"


    frase = f"""
        Seu nome é {nome_usuario}
        Você tem {idade_usuario} anos
        Seu nome invertido é {nome_usuario[::-1]}
        {espacos}
        A primeira letra do seu nome é \"{nome_usuario[0].lower()}\"
        A última letra do seu nome é \"{nome_usuario[-1].lower()}\"
   """

    print(frase)
    
else:
    print("Desculpe, você deixou os campos vazios")

