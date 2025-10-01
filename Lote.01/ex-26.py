#Receba dois números inteiros, verifique e mostre se o maior é múltiplo do menor.
#Gabriella da Silva

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

if maior % menor == 0:
    print("O maior número é múltiplo do menor.")
else:
    print("O maior número não é múltiplo do menor.")