#Receba um valor inteiro e verifique se é divisível por 3 e 2.
#Gabriella da Silva

Num = int(input("Digite um número inteiro: "))

if Num % 3 == 0:
    print("O número é divisível por 3")
else:
    print("O número não é divisível por 3")

if Num % 2 == 0:
    print("O número é divisível por 2")
else:
    print("O número não é divisível por 2")