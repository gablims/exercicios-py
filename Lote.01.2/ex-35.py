#Receba dois números inteiros, verifique o maior. Calcule e mostre 
#o resultado da somatória dos números ímpares entre eles.
#Modularizado.
#Gabriella da Silva

Num1 = int(input("Digite um número inteiro: "))
Num2 = int(input("Digite outro número inteiro: "))

def calcSomaImpares ():
    if Num1 > Num2:
        maior = Num1
        menor = Num2
    else:
        maior = Num2
        menor = Num1
    soma = 0
    for i in range(menor + 1, maior):
        if i % 2 != 0:
            soma += i
    return soma
print(f"A soma dos números ímpares entre {Num1} e {Num2} é: {calcSomaImpares()}")