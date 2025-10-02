#Receba um valor inteiro e verifique se é divisível por 3 e 2.
#Modularizado.
#Gabriella da Silva

Num = int(input("Digite um número inteiro: "))

def calcDiv ():
    if Num % 3 == 0 and Num % 2 == 0:
        return True
    else:
        return False

if calcDiv():
    print(f"O número {Num} é divisível por 3 e por 2.")
else:
    print(f"O número {Num} não é divisível por 3 e por 2.")