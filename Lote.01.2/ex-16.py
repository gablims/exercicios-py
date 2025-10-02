#Receba a quantidade de horas trabalhadas, o valor por hora, o percentural de desconto e o 
#número de dependentes. Calcule e mostre o salário líquido.
#Modularizado. 
#Gabriella da Silva

Horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
Valor_hora = float(input("Digite o valor por hora: "))
Percentual_desconto = float(input("Digite o percentual de desconto: "))
Numero_dependentes = int(input("Digite o número de dependentes: "))

def calcSal ():
    salario_bruto = Horas_trabalhadas * Valor_hora
    desconto = salario_bruto * (Percentual_desconto / 100)
    adicional_dependentes = Numero_dependentes * 50  # Supondo um adicional fixo por dependente
    salario_liquido = salario_bruto - desconto + adicional_dependentes
    return salario_liquido

print(f"O salário líquido é: R$ {calcSal():.2f}")