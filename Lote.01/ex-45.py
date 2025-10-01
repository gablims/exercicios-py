#Calcule e mostre a série 1 - 2/4 + 3/9 + 4/16 + 5/25 + ... + 15/225.
#Gabriella da Silva

soma = 0
for i in range(1, 16):
    soma += ((-1) ** (i + 1)) * (i / (i * i))
print(f"A soma da série é: {soma}")