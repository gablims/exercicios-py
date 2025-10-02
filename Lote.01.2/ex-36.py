#Receba um número N, calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!.
#Modularizado.
#Gabriella da Silva

num = int(input("Digite um número inteiro positivo: "))

def calcSerieFatorial (n=num):
    if n < 0:
        return "Número inválido. Digite um número inteiro positivo."
    serie = 0
    fat = 1
    for i in range(0, n + 1):
        if i > 0:
            fat *= i
        serie += 1 / fat
    return serie
print(f"O valor da série 1 + 1/1! + 1/2! + ... + 1/{num}! é: {calcSerieFatorial(num):.2f}")