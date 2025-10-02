#Receba 2 números inteiros, verifique e mostre todos os números primos entre eles.
#Modularizado.
#Gabriella da Silva

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

def calcPrimos (num1=n1, num2=n2):
    if num1 > num2:
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1
    primos = []
    for num in range(menor, maior + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primos.append(num)
    return primos
print(f"Os números primos entre {n1} e {n2} são: {calcPrimos(n1, n2)}")