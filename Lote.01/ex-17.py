#Calcule a quantidade de litros gastos em uma viagem, sabendo que o carro faz 12km com 1 litro.
#Receber tempo de percurso e velocidade média.
#Gabriella da Silva

tempo = float(input("Digite o tempo gasto na viagem em horas: "))
velocidade = float(input("Digite a velocidade média em km/h: "))

distancia = velocidade * tempo
litrosGastos = distancia / 12

print("A quantidade de litros gastos na viagem é de: ", litrosGastos)