#Receba 100 números reais, verifique o maior e o manor valor. Obs: Somente valor positivo.
#Gabriella da Silva

maior = 0
menor = None

for i in range(1, 101):
    num = float(input("Digite número real positivo: "))

    while num < 0:
        num = float(input("Número inválido. Digite número real positivo: "))
    if num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')