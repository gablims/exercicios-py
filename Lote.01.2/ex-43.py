#Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que
#Ana tem 1,10m e cresce 3cm por ano e Maria tem 1,50m e cresce 2cm por ano.
#Modularizado.
#Gabriella da Silva

def calcAnos ():
    alturaAna = 1.10
    alturaMaria = 1.50
    anos = 0
    while alturaAna <= alturaMaria:
        alturaAna += 0.03
        alturaMaria += 0.02
        anos += 1
    return anos
print(f"Serão necessários {calcAnos()} anos para que Ana seja maior que Maria.")