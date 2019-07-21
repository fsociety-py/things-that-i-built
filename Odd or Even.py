#-----------------------------------------------------------------------------------------------------------------------
# Máquina-V1

number = int(input("Digite um número para verificar se é par ou ímpar: "))
if number % 2 == 0:
    print("O número {} é par!" .format(number))
else:
    print("O número {} é ímpar!" .format(number))
#-----------------------------------------------------------------------------------------------------------------------
# Máquina-V2

number2 = int(input("Digite um número para verificar se é par, ímpar ou multiplo de 4: "))
if number2 % 4 == 0:
    print("O número {} é par e multiplo de 4!" .format(number2))
elif number2 % 2 == 0:
    print("O número {} é par!" .format(number2))
else:
    print("O número {} é ímpar!" .format(number2))
#-----------------------------------------------------------------------------------------------------------------------
# Máquina-V3

number3 = int(input("Digite um número para checar: "))
divide = int(input("Digite um divisor: "))
result = number3 / divide
if number3 % divide == 0:
    print("O número {} divide o número {} resultando em {} que é um quociente par e um número inteiro." .format(number3, divide, result))
elif number3 % divide != 0:
    print("O número {} divide o número {} resultando em {} que é um quociente ímpar." .format(number3, divide, result))
else:
    print("O número {} divide o número {} resultando em {} que é um quociente par." .format(number3, divide, result))
