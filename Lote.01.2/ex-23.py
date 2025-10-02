#Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem.
#Mostre os 4 valores em ordem crescente.
#Modularizado.
#Gabriella da Silva

Num1 = int(input("Digite um número inteiro: "))
Num2 = int(input("Digite outro número inteiro maior que o primeiro: "))
Num3 = int(input("Digite outro número inteiro maior que o segundo: "))
Num4 = int(input("Digite outro número inteiro: "))

def calcOrdem ():
    lista = [Num1, Num2, Num3, Num4]
    lista.sort()
    return lista
print(f"Números em ordem crescente: {calcOrdem()[0]}, {calcOrdem()[1]}, {calcOrdem()[2]} e {calcOrdem()[3]}")