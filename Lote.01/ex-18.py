#Receba dois valores inteiros, calcule e mostre a diferença do maior pelo menor.
#Gabriella da Silva

Num1 = int(input("Digite um número inteiro: "))
Num2 = int(input("Digite outro número inteiro: "))

if Num1 > Num2:
    maior = Num1
    menor = Num2
else:
    maior = Num2
    menor = Num1

diferenca = maior - menor
print("A diferença do maior pelo menor é:", diferenca)