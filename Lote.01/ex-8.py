#Vamos calcular o valor de um depósito após um mês de rendimento?

deposito: float
rendimento: float
valorFinal: float

deposito = float(input("Digite o valor do depósito: "))

rendimento = deposito*0.013
valorFinal = deposito+rendimento

print("O valor após um mês de rendimento é de: ", valorFinal)