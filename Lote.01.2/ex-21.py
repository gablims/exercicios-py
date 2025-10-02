#Receba 4 notas bimestrais, calcule e mostre sua média aritmética. 
#Modularizado.
#Gabriella da Silva

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

def calcMedia ():
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

if calcMedia() >= 6:
    print(f"Sua média é: {calcMedia():.2f}. Você foi aprovado(a)!")
elif calcMedia() < 6 and calcMedia() >= 3:
    print(f"Sua média é: {calcMedia():.2f}. Você fará o teste.")
else:
    print(f"Sua média é: {calcMedia():.2f}. Você foi reprovado(a).")