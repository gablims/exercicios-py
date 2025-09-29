#Tendo velocidade média, tempo de viagem e sabendo que um automóvel faz
#12 km por litro de combustível, calcular quantos litros serão gastos na viagem
#Gabriella da Silva

velocidadeMedia = float(input("Digite a velocidade média (em km/h): "))
tempo = float(input("Digite o tempo (em horas): "))

distancia = velocidadeMedia * tempo
litrosGastos = distancia / 12

print("A quantidade de litros gastos na viagem será: ", litrosGastos)