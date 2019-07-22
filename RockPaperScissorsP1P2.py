print("Bem vindo ao jogo Pedra, Papel ou Tesoura!!!")
stop = False
while not stop:
    answerP1 = input("Player 1: Pedra, Papel ou Tesoura?\n")
    answerP2 = input("Player 2: Pedra, Papel ou Tesoura?\n")
    if answerP1 == answerP2:
        print("Empate!!!")
    elif answerP1 == 'Pedra' and answerP2 == 'Papel':
        print('Pedra vs Papel:\nPlayer 2 Ganhou!!!')
    elif answerP1 == 'Pedra' and answerP2 == 'Tesoura':
        print('Pedra vs Tesoura:\nPlayer 1 Ganhou!!!')
    elif answerP1 == 'Papel' and answerP2 == 'Pedra':
        print('Papel vs Pedra:\nPlayer 1 Ganhou!!!')
    elif answerP1 == 'Papel' and answerP2 == 'Tesoura':
        print('Papel vs Tesoura:\nPlayer 2 Ganhou!!!')
    elif answerP1 == 'Tesoura' and answerP2 == 'Pedra':
        print('Tesoura vs Pedra:\nPlayer 2 Ganhou!!!')
    elif answerP1 == 'Tesoura' and answerP2 == 'Papel':
        print('Tesoura vs Papel:\nPlayer 1 Ganhou!!!')
    else:
        print('Desculpe, por favor escolha entre Pedra, Papel ou Tesoura e tente novamente!')
    answer = input('Quer começar um novo jogo? (Sim ou Não)\n')
    if answer == "Sim":
        print("Um novo jogo irá começar!")
    elif answer == "Não":
        print("GAME OVER")
        stop = True
    else:
        print("Desculpe, por favor escolha entre Sim ou Não e tente novamente!")
