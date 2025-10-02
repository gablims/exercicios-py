#Receba um número, calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/n.
#Modularizado.
#Gabriella da Silva

num = int(input("Digite um número inteiro positivo: "))

def calcSerie (n=num):
    if n <= 0:
        return "Número inválido. Digite um número inteiro positivo."
    serie = 0
    for i in range(1, n + 1):
        serie += 1 / i
    return serie

print(f"O valor da série 1 + 1/2 + 1/3 + ... + 1/{num} é: {calcSerie(num):.2f}")