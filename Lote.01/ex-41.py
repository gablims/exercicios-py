#Mostre a possibilidade de 2 dados de forma que a soma tenha como resultado 7.
#Gabriella da Silva

lados = 6

lista = []

for num1 in range(lados+1):
    for num2 in range(lados+1):
        if num1 + num2 == 7:
            lista.append((num1,num2)) 

print(lista)