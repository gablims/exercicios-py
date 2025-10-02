#Receba dois valores inteiros, calcule e mostre a diferença do maior pelo menor.
#Modularizado.
#Gabriella da Silva

Num1 = int(input("Digite um número inteiro: "))
Num2 = int(input("Digite outro número inteiro: "))

def calcDif ():
    if Num1 > Num2:
        diferenca = Num1 - Num2
    else:
        diferenca = Num2 - Num1
    return diferenca

print(f"A diferença entre o maior e o menor número é: {calcDif()}")