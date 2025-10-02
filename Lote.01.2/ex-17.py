#Calcule a quantidade de litros gastos em uma viagem, sabendo que o carro faz 12km com 1 litro.
#Receber tempo de percurso e velocidade média.
#Modularizado.
#Gabriella da Silva

Tempo_percurso = float(input("Digite o tempo de percurso (em horas): "))
Velocidade_media = float(input("Digite a velocidade média (em km/h): "))

def calcLitros ():
    distancia = Tempo_percurso * Velocidade_media
    litros_gastos = distancia / 12  
    return litros_gastos

print(f"A quantidade de litros gastos na viagem é: {calcLitros():.2f} litros")