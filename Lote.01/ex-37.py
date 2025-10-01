#Receba um número inteiro, calcule e mostre a série fibonacci até o N-ésimo termo.
#Gabriella da Silva

num = int(input("Digite um número inteiro positivo: "))
termo1 = 0
termo2 = 1
contador = 1

print(f'Série de Fibonacci até o {num}° termo: ', end='')
while contador <= num:
    if contador == 1:
        print(termo1, end=' ')
    elif contador == 2:
        print(termo2, end=' ')
    else:
        termo3 = termo1 + termo2
        print(termo3, end=' ')
        termo1 = termo2
        termo2 = termo3
    contador += 1