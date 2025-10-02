#Receba 100 números reais, verifique o maior e o menor valor. Obs: Somente valor positivo.
#Modularizado.
#Gabriella da Silva

def calcMaiorMenor ():
    maior = 0
    menor = None
    for _ in range(100):
        num = float(input("Digite um número real (positivo): "))
        if num < 0:
            print("Número inválido. Digite apenas números positivos.")
            continue
        if num > maior:
            maior = num
        if menor is None or num < menor:
            menor = num
    return maior, menor
maior, menor = calcMaiorMenor()
print(f"O maior número é: {maior} e o menor número é: {menor}")