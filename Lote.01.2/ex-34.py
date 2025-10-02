#Receba um número inteiro, calcule e mostre a tabuada desse número.
#Modularizado.
#Gabriella da Silva

num = int(input("Digite um número inteiro para ver a sua tabuada: "))

def calcTabuada (n=num):
    tabuada = []
    for i in range(1, 11):
        tabuada.append(f"{n} x {i} = {n * i}")
    return tabuada
print(f"A tabuada do {num} é:")
for linha in calcTabuada():
    print(linha)