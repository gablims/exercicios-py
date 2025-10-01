#Receba um número inteiro, calcule e mostre a tabuada desse número.
#Gabriella da Silva

num = int(input("Digite um número inteiro para ver a sua tabuada: "))

I = 1 
while I <= 10:
    R = num * I
    I = I + 1
    print(R)