#Receba um número inteiro, calcule e mostre o seu fatorial.
#Gabriella da Silva

fat = 1
num = int(input("Digite um número inteiro para calcular o seu fatorial: "))

while num > 1:
    fat = fat * num
    num = num - 1
print("O fatorial desse número é", fat)