#Receba 4 notas bimestrais, calcule e mostre a média anual 
#e mostre a mensagem de acordo com a média. 
#Gabriella da Silva

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print("Aprovado! Sua média anual é: ", media)
elif media >= 3 and media < 6: 
    print("Recuperação! Sua média anual é: ", media)
elif media < 3:
    print("Reprovado! Sua média anual é: ", media) 
else:
    print("Erro! Sua média não pode ser calculada.")  