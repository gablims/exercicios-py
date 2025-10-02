#Receba dois valores reais, calcule e mostre o maior deles.
#Modularizado.
#Gabriella da Silva

Num1 = float(input("Digite um número real: "))
Num2 = float(input("Digite outro número real: "))

def calcMaior ():
    if Num1 > Num2:
        maior = Num1
    else:
        maior = Num2
    return maior

print(f"O maior número é: {calcMaior()}")