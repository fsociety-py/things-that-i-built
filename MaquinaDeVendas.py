import sys
order = int(input(
    """
Bem vindo a Loja de Vendas!!!
1.Guaraná Antarctica - $1.00
2.Coca-Cola - $ 1.50
3.Energético RedBull - $2.00
Escolha o numero do pedido (1, 2, 3...)
    """
                  ))
if order == 1:
    disPrice = 1.00
    print("Você escolheu Guaraná Antarctica.")
elif order == 2:
    disPrice = 1.50
    print("Você escolheu Coca-Cola.")
elif order == 3:
    disPrice = 2.00
    print("Você escolheu Energético RedBull.")
else:
    sys.exit("Por favor tente novamente.")
vinte_cinco_centavos = int(input("Coloque o tanto de moedas de 25c."))
dez_centavos = int(input("Coloque o tanto de moedas de 10c."))
cinco_centavos = int(input("Coloque o tanto de moedas de 5c."))
total = ((vinte_cinco_centavos * 0.25) + (dez_centavos * 0.10) + (cinco_centavos * 0.05))
print("O total que você colocou é $%.2f" %(total))
if total >= disPrice:
    print("Seu troco é $" + "%.2f" % (total - disPrice) + ". Tenha um bom dia.")
else:
    print("Volte quando tiver dinheiro.")
