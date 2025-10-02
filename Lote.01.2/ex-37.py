#Receba um número inteiro, calcule e mostre a série fibonacci até o N-ésimo termo.
#Modularizado.
#Gabriella da Silva

num = int(input("Digite um número inteiro positivo: "))

def calcFibonacci (n=num):
    if n <= 0:
        return "Número inválido. Digite um número inteiro positivo."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci = [0, 1]
        for i in range(2, n):
            proximo = fibonacci[i - 1] + fibonacci[i - 2]
            fibonacci.append(proximo)
        return fibonacci
print(f"A série Fibonacci até o {num}-ésimo termo é: {calcFibonacci(num)}")