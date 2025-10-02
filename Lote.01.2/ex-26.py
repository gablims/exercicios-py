#Receba dois números inteiros, verifique e mostre se o maior é múltiplo do menor.
#Modularizado.
#Gabriella da Silva

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

def calcMult ():
    if num1 > num2:
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1
    if maior % menor == 0:
        return True, maior, menor
    else:
        return False, maior, menor

if calcMult()[0]:
    print(f"O número {calcMult()[1]} é múltiplo do número {calcMult()[2]}.")
else:
    print(f"O número {calcMult()[1]} não é múltiplo do número {calcMult()[2]}.")