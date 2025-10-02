#Receba o tipo de investimento, (1 = poupança e 2 = renda fixa) e o valor investido. Calcule e mostre
#o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.
#Modularizado.
#Gabriella da Silva

tipo_investimento = int(input("Digite o tipo de investimento (1 = poupança, 2 = renda fixa): "))
valor_investido = float(input("Digite o valor investido: "))

def calcInvestimento ():
    if tipo_investimento == 1:
        valor_corrigido = valor_investido * 1.03  
    elif tipo_investimento == 2:
        valor_corrigido = valor_investido * 1.05  
    else:
        return "Tipo de investimento inválido."
    return valor_corrigido
print(f"O valor corrigido após 30 dias é: R$ {calcInvestimento():.2f}")