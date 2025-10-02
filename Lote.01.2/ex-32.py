#Receba um número inteiro, calcule e mostre o seu fatorial.
#Modularizado.
#Gabriella da Silva

num = int(input("Digite um número inteiro para calcular o seu fatorial: "))

def calcFatorial (n=num):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat
resultado = calcFatorial()
print(f"O fatorial de {num} é: {resultado}")