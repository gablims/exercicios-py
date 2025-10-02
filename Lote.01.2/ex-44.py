#Receba o número da base e do expoente, calcule e mostre o valor da potência.
#Modularizado.
#Gabriella da Silva

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

def calcPotencia (b=base, e=expoente):
    potencia = b ** e
    return potencia
print(f"O valor de {base} elevado a {expoente} é: {calcPotencia(base, expoente)}")