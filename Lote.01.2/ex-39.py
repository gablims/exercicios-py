#Calcule a quantidade de grãos contidos em um tabuleiro de xadres, onde:
#Casa: 1 2 3 4 ... 64
#Qdte: 1 2 4 8 ... N
#Modularizado.
#Gabriella da Silva

num = 64
def calcGrains (n=num):
    grains = 1
    total = 0
    for i in range(1, n + 1):
        total += grains
        grains *= 2
    return total
print(f"A quantidade total de grãos no tabuleiro de xadrez é: {calcGrains()}")