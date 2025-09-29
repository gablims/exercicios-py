#Receba os 3 coeficiantes de uma equação do 2º grau 
#e caso exista, mostre suas raízes.
#Gabriella da Silva

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
delta = (B ** 2) - (4 * A * C)
raizDelta = delta ** 0.5

if delta < 0:
    print("A equação não possui raizes reais")
elif delta == 0:
    raiz = -B / (2 * A)
    print("A equação possui uma raiz real: ", raiz)
elif delta > 0:
    raiz1 = (-B + raizDelta) / (2 * A)
    raiz2 = (-B - raizDelta) / (2 * A)
    print("A equação possui duas raizes reais: ", raiz1, " e ", raiz2)
else:
    print("Erro! As raízes não podem ser calculadas.")