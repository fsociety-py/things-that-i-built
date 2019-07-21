import datetime
nome = input("Digite seu nome:\n")
idade = int(input("Digite sua idade:\n"))
ano_atual = datetime.datetime.now()
ageCen = int(ano_atual.year + 100 - idade)
print("Hey " + nome + " você terá 100 anos em " + str(ageCen))