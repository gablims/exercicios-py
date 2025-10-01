#Receba o tipo de investimento, (1 = poupança e 2 = renda fixa) e o valor investido. Calcule e mostre
#o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.
#Gabriella da Silva

tipo_investimento = int(input("Digite o tipo de investimento (1 = poupança, 2 = renda fixa): "))
valor_investido = float(input("Digite o valor investido: "))

if tipo_investimento == 1:
    valor_corrigido = valor_investido * 1.03
    print(f"O valor corrigido após 30 dias na poupança é: R$ {valor_corrigido:.2f}")
elif tipo_investimento == 2:
    valor_corrigido = valor_investido * 1.05
    print(f"O valor corrigido após 30 dias na renda fixa é: R$ {valor_corrigido:.2f}")
else:
    print("Tipo de investimento não é válido. Apenas poupança (1) e renda fixa (2) são considerados.")