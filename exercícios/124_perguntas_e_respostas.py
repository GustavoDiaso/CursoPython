# Exercício - sistema de perguntas e respostas


def game():
    questions = [
        {
            "question": "Quanto é 2+2?",
            "options": ["1", "3", "4", "5"],
            "answer": "4",
        },
        {
            "question": "Quanto é 5*5?",
            "options": ["25", "55", "10", "51"],
            "answer": "25",
        },
        {
            "question": "Quanto é 10/2?",
            "options": ["4", "5", "2", "1"],
            "answer": "5",
        },
    ]

    q = 0

    while q < 3:

        print(f"{questions[q]['question']}\n")
        print(f"{questions[q]['options']}")
        answer = input("R:")

        if answer == questions[q]["answer"]:
            print("\nVocê acertou! 👍👍👍\n")
            q += 1

        else:
            print("\nVocê errou! Tente novamente 🙁☹️\n")

    print("Parabéns, você ganhou o jogo")


game()
