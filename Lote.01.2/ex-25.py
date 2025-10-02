#Receba a hora início e final de um jogo (HH,MM), calcule a duração do jogo em horas e minutos,
# sabendo que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode começar em um dia e terminar no outro.
#Modularizado.
#Gabriella da Silva

horaInicio = int(input("Digite a hora de início do jogo (0-23): "))
minutoInicio = int(input("Digite o minuto de início do jogo (0-59): "))
horaFinal = int(input("Digite a hora de término do jogo (0-23): "))
minutoFinal = int(input("Digite o minuto de término do jogo (0-59): "))

def calcDuracao ():
    inicioEmMinutos = horaInicio * 60 + minutoInicio
    finalEmMinutos = horaFinal * 60 + minutoFinal

    if finalEmMinutos <= inicioEmMinutos:
        finalEmMinutos += 24 * 60  

    duracaoEmMinutos = finalEmMinutos - inicioEmMinutos
    duracaoHoras = duracaoEmMinutos // 60
    duracaoMinutos = duracaoEmMinutos % 60

    return duracaoHoras, duracaoMinutos
duracaoHoras, duracaoMinutos = calcDuracao()
print(f"A duração do jogo foi de {duracaoHoras} horas e {duracaoMinutos} minutos.")