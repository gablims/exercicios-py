#Receba dois valores inteiros e diferentes, mostre-os em ordem crescente.
#Gabriella da Silva

Valor1 = int(input("Digite o primeiro valor: "))
Valor2 = int(input("Digite o segundo valor: "))

if Valor1 < Valor2:
   crescente = Valor1, Valor2
elif Valor1 == Valor2:
    crescente = "Os dois valores são iguais"
elif Valor1 > Valor2:
    crescente = Valor2, Valor1
else:
    crescente = "Erro! Não há uma ordem crescente" 

print("Os valores em ordem crescente são: ", crescente)