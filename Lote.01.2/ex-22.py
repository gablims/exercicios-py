#Receba dois valores inteiros e diferentes. Mostre-os em ordem crescente.
#Modularizado.
#Gabriella da Silva

Num1 = int(input("Digite um número inteiro: "))
Num2 = int(input("Digite outro número inteiro: "))

def calcOrdem ():
    if Num1 < Num2:
        return Num1, Num2
    else:
        return Num2, Num1
print(f"Números em ordem crescente: {calcOrdem()[0]} e {calcOrdem()[1]}")