#Receba os coeficientes A,B e C de uma equação de 2° grau da fórmula Ax² + Bx + C = 0.
#Verifique se existem raízes reais e se existirem, calcule e mostre o valor delas.
#Gabriella da Silva
import math

A = float(input("Digite o valor do coeficiente A: "))
B = float(input("Digite o valor do coeficiente B: "))
C = float(input("Digite o valor do coeficiente C: "))

delta = B**2 - 4 * A * C
if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    raiz = -B / (2 * A)
    print(f"A raiz da equação é: {raiz:.2f}")
else:
    raiz1 = (-B + math.sqrt(delta)) / (2 * A)
    raiz2 = (-B - math.sqrt(delta)) / (2 * A)
    print(f"As raízes da equação são: {raiz1:.2f} e {raiz2:.2f}")