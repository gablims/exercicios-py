#Mostre a possibilidade de 2 dados de forma que a soma tenha como resultado 7.
#Modularizado.
#Gabriella da Silva

def calcDados ():
    possibilidades = []
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            if dado1 + dado2 == 7:
                possibilidades.append((dado1, dado2))
    return possibilidades
print("As possibilidades de dois dados cuja soma é 7 são:")
for par in calcDados():
    print(par)