print("Vamos descobrir quantos dias vai durar uma quantidade de alimento para uma pessoa que come 50g por dia.")

quilos: float
dias: float

quilos = float(input("Digite uma quantidade de comida em quilos: "))

dias = (quilos*1000) / 50 

print("A quantidade de dias que essa quantidade de comida irá durar é: ", dias)