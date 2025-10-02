#Receba os coeficientes A,B e C de uma equação de 2° grau da fórmula Ax² + Bx + C = 0.
#Verifique se existem raízes reais e se existirem, calcule e mostre o valor delas.
#Modularizado.
#Gabriella da Silva
import math

A = float(input("Digite o valor do coeficiente A: "))
B = float(input("Digite o valor do coeficiente B: "))
C = float(input("Digite o valor do coeficiente C: "))

def calcRaizes ():
    delta = B**2 - 4*A*C
    if delta < 0:
        return None
    elif delta == 0:
        raiz = -B / (2*A)
        return (raiz,)
    else:
        raiz1 = (-B + math.sqrt(delta)) / (2*A)
        raiz2 = (-B - math.sqrt(delta)) / (2*A)
        return (raiz1, raiz2)
raizes = calcRaizes()

if raizes is None:
    print("Não existem raízes reais.")
elif len(raizes) == 1:
    print(f"Existe uma raiz real: {raizes[0]:.2f}")
else:
    print(f"Existem duas raízes reais: {raizes[0]:.2f} e {raizes[1]:.2f}")