def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas >= 150:
        salario = horas * taxa
    else:
        h_exc = horas - 150
        salario = 150 * taxa + (h_exc*(1.5*taxa))
    return salario


str_horas = input("Digite a quantidade de horas: ")
str_taxa = input("Digite o valor da hora: ")
total_salario = calcular_pagamento(str_horas, str_taxa)
print("O valor de seus rendimentos é R$", total_salario)
