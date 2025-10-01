#Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que
#Ana tem 1,10m e cresce 3cm por ano e Maria tem 1,50m e cresce 2cm por ano.
#Gabriella da Silva

altura_ana = 1.10
altura_maria = 1.50
anos = 0

while altura_ana <= altura_maria:
    altura_ana += 0.03
    altura_maria += 0.02
    anos += 1
print(f"Serão necessários {anos} anos para que Ana seja maior que Maria.")