import math
#Vamos calcular a hipotenusa de um triângulo retângulo?

catetoUm: float
catetoDois: float
catetos: float
hipotenusa: float

catetoUm = float(input("Digite o valor do primeiro cateto: "))
catetoDois = float(input("Digite o valor do segundo cateto: "))

catetos = ((catetoUm*catetoUm)+(catetoDois*catetoDois))
hipotenusa = math.sqrt(catetos)

print("O valor da hiptenusa do seu triângulo retângulo é: ", hipotenusa)