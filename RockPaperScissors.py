from random import randint
print("Bem vindo ao jogo Pedra, Papel ou Tesoura!!!")
t = ["Pedra", "Papel", "Tesoura"]
computer = t[randint(0, 2)]
stop = False
while not stop:
    player = input("Escolha entre Pedra, Papel ou Tesoura?\n")
    if player == computer:
        print("Empate!!!")
    elif player == "Pedra":
        if computer == "Papel":
            print("Você perdeu!!!", computer, "cobre", player)
        else:
            print("Você ganhou!!!", player, "esmaga", computer)
    elif player == "Papel":
        if computer == "Pedra":
            print("Você ganhou!!!", player, "cobre", computer)
        else:
            print("Você perdeu!!!", computer, "corta", player)
    elif player == "Tesoura":
        if computer == "Pedra":
            print("Você perdeu!!!", computer, "esmaga", player)
        else:
            print("Você ganhou!!!", player, "corta", computer)
    else:
        print("Desculpe, palavra errada, tente novamente.")
        continue
    answer = input('Quer começar um novo jogo? (Sim ou Não)\n')
    if answer == "Sim":
        print("Um novo jogo irá começar!")
        stop = False
    elif answer == "Não":
        print("GAME OVER")
        stop = True
    else:
        print("Desculpe, por favor escolha entre Sim ou Não e tente novamente!")
        while answer != "Sim" and "Não":
            answer = input('Quer começar um novo jogo? (Sim ou Não)\n')
    computer = t[randint(0, 2)]
