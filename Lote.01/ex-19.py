#Receba dois valores reais, calcule e mostre o maior deles.
#Gabriella da Silva

Num1 = float(input("Digite um número real: "))
Num2 = float(input("Digite outro número real: "))

if Num1 > Num2:
    maior = Num1
else:
    maior = Num2

print("O maior número é:", maior)