#Calcule a quantidade de grãos contidos em um tabuleiro de xadres, onde:
#Casa: 1 2 3 4 ... 64
#Qdte: 1 2 4 8 ... N
#Gabriella da Silva

casa = 1
grãos = 1
total = 0

while casa <= 64:
    total += grãos
    grãos *= 2
    casa += 1
print (f'A quantidade total de grãos no tabuleiro é: {total}')
print (f'A quantidade de grãos na 64ª casa é: {grãos // 2}')