#Receba dois valores inteiros e diferentes. Mostre-os em ordem crescente.
#Gabriella da Silva

Num1 = int(input("Digite um número inteiro: "))
Num2 = int(input("Digite outro número inteiro: "))

if Num1 < Num2:
    print("Os números em ordem crescente são:", Num1, ",", Num2)
else:
    print("Os números em ordem crescente são:", Num2, ",", Num1)