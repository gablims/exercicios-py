#Receba 2 números inteiros, verifique e mostre todos os números primos entre eles.
#Gabriella da Silva

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

if n1 > n2:
    n1, n2 = n2, n1
print(f"Números primos entre {n1} e {n2}:")
num = n1

while num <= n2:
    if num > 1:
        i = 2
        primo = True
        while i <= num // 2:
            if num % i == 0:
                primo = False
                break
            i += 1
        if primo:
            print(num, end=' ')
    num += 1