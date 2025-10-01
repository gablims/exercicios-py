#Calcule o valor do 3° ângulo de um retângulo, já tendo dois ângulos.
#Gabriella da Silva

anguloUm = float(input("Digite o valor do primeiro ângulo: "))
anguloDois = float(input("Digite o valor do segundo ângulo: "))

anguloTres = 180 - (anguloUm + anguloDois)

print("O valor do terceiro ângulo é: ", anguloTres)