#Receba dois números inteiros, verifique o maior. Calcule e mostre 
#o resultado da somatória dos números ímpares entre eles.
#Gabriella da Silva

Num1 = int(input("Digite um número inteiro: "))
Num2 = int(input("Digite outro número inteiro: "))
soma = 0

if Num1 > Num2:
    for Num in range(Num2 + 1, Num1):
        if Num % 2 != 0:
            soma += Num
elif Num2 > Num1:
    for Num in range(Num1 + 1, Num2):
        if Num % 2 != 0:
            soma += Num
else:
    print("Os números digitados são iguais.")

print("A soma dos números ímpares entre eles é", soma)