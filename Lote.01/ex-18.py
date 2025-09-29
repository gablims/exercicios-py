#Receba dois valores inteiros, calcule e mostre a diferença do maior pelo menor.
#Gabriella da Silva

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
     diferenca = valor1 - valor2
elif valor1 == valor2:
    diferenca = 0
elif valor1 < valor2:
    diferenca = valor2 - valor1
else:
    diferenca = "Erro! Não foi possível identificar a diferença"

print("A diferença do maior pelo menor é: ", diferenca)
