#Receba a hora início e final de um jogo (HH,MM), calcule a duração do jogo em horas e minutos,
# sabendo que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode começar em um dia e terminar no outro.
#Gabriella da Silva

horaInicio = int(input("Digite a hora de início do jogo (0-23): "))
minutoInicio = int(input("Digite o minuto de início do jogo (0-59): "))
horaFinal = int(input("Digite a hora de término do jogo (0-23): "))
minutoFinal = int(input("Digite o minuto de término do jogo (0-59): "))

duracao_hora = 0
duracao_minutos = 0

if minutoFinal >= minutoInicio:
    duracao_minutos = minutoFinal - minutoInicio
else:
    duracao_hora -=1
    duracao_minutos = minutoInicio - minutoFinal

if horaFinal > horaInicio:
    duracao_hora += horaFinal - horaInicio
else:
    duracao_hora += (horaFinal+24) -horaInicio

print("A duração do jogo é de", duracao_hora, "horas e", duracao_minutos, "minutos.")