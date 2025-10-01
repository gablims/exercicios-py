#Vamos efetuar a troca de dois valores diferentes e ver os valores finais.
#Gabriella da Silva

X = float(input("Digite o valor de X:"))
Y = float(input("Digite o valor de Y:"))

Intermediaria = X
X = Y
Y = Intermediaria

print("O valor de X e Y são, respectivamente: ", X, Y)
