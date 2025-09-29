#Receba dois valores, calcule e mostre o maior deles.
#Gabriella da Silva

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    maior = valor1
elif valor1 == valor2:
    maior = "Os dois valores são iguais"
elif valor1 < valor2:
    maior = valor2
else:
    maior = "Erro! Não foi possível identificar o maior valor"

print("O maior valor é: ", maior)