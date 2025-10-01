#Receba 4 notas bimestrais, calcule e mostre sua média aritmética. 
#Gabriella da Silva

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6: 
    print("Aprovado, sua média é:", media)
elif media >= 3 and media < 6:
    print("Exame, sua média é:", media)
else:
    print("Reprovado, sua média é:", media)