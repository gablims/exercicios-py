#Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem.
#Mostre os 4 valores em ordem crescente.
#Gabriella da Silva

Num1 = int(input("Digite um número inteiro: "))
Num2 = int(input("Digite outro número inteiro maior que o primeiro: "))
Num3 = int(input("Digite outro número inteiro maior que o segundo: "))
Num4 = int(input("Digite outro número inteiro: "))

if Num4 < Num1:
    print("Os números em ordem crescente são:", Num4, ",", Num1, ",", Num2, ",", Num3)
elif Num4 < Num2:
    print("Os números em ordem crescente são:", Num1, ",", Num4, ",", Num2, ",", Num3)
elif Num4 < Num3:
    print("Os números em ordem crescente são:", Num1, ",", Num2, ",", Num4, ",", Num3)
else:
    print("Os números em ordem crescente são:", Num1, ",", Num2, ",", Num3, ",", Num4)