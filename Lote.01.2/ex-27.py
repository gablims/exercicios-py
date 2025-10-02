#Receba o número de voltas, a extensão do circuito (em metros) e o tempo (minutos) de uma corrida de Fórmula 1.
#Calcule e mostre a velocidade média em km/h.
#Modularizado.
#Gabriella da Silva

num_voltas = int(input("Digite o número de voltas: "))
extensao_circuito = float(input("Digite a extensão do circuito (em metros): "))
tempo_minutos = float(input("Digite o tempo da corrida (em minutos): "))

def calcVelocidade ():
    distancia_total_km = (num_voltas * extensao_circuito) / 1000  
    tempo_horas = tempo_minutos / 60  
    velocidade_media = distancia_total_km / tempo_horas  
    return velocidade_media
print(f"A velocidade média da corrida foi: {calcVelocidade():.2f} km/h")