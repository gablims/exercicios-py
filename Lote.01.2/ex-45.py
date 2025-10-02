#Calcule e mostre a série 1 - 2/4 + 3/9 + 4/16 + 5/25 + ... + 15/225.
#Modularizado.
#Gabriella da Silva

def calcSerie ():
    serie = 0
    for i in range(1, 16):
        if i % 2 == 0:
            serie -= i / (i * i)
        else:
            serie += i / (i * i)
    return serie
print(f"O valor da série 1 - 2/4 + 3/9 + 4/16 + ... + 15/225 é: {calcSerie():.2f}")