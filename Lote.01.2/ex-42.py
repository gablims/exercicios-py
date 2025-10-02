#Calcule e mostre a série 1 + 2/3 + 3/5 + ... 50/99.
#Modularizado.
#Gabriella da Silva

def calcSerie ():
    serie = 0
    denominador = 1
    for numerador in range(1, 51):
        serie += numerador / denominador
        denominador += 2
    return serie
print(f"O valor da série 1 + 2/3 + 3/5 + ... + 50/99 é: {calcSerie():.2f}")