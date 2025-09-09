import math
print("Considerando que uma equação tem duas raízes, vamos calcular e descobrir quais são os valores de suas raízes")

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

Delta = ((B*B) -4*A*C)
RaizDelta = math.sqrt(Delta)
X1 = (-B+RaizDelta) / (2*A)
X2 = (-B-RaizDelta) / (2*A)

print("Os valores de X1 e de X2 são, respectivamente: ", X1, X2)
