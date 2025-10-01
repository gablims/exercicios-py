#Receba um número N, calcule e morte a série 1 + 1/1! + 1/2! + ... + 1/N!.
#Gabriella da Silva

num = int(input("Digite um número inteiro positivo: "))

contador = 1
soma = 1
fatorial = 1

while contador <= num:
    fatorial *= contador
    soma += 1 / fatorial
    contador += 1

print (f'O resultado da série é: {soma:.4f}')