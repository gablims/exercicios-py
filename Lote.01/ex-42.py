#Calcule e mostre a série 1 + 2/3 + 3/5 + ... 50/99.
#Gabriella da Silva

soma = 0
for i in range(1, 51):
    soma += i / (2 * i - 1)
print(f"A soma da série é: {soma}")