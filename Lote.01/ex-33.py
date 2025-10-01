#Receba um número, calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/n.
#Gabriella da Silva

num = int(input("Digite um número inteiro positivo: "))

contador = 1
soma = 0

while contador <= num:
    soma += 1 / contador
    contador += 1
print (f'O resultado da série é: {soma:.4f}')