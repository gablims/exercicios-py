#Vamos calcular um salário.
#Gabriella da Silva

Horas = float(input("Digite o número de horas trabalhadas no mês: "))
ValorHora = float(input("Digite o valor que você recebe por hora trabalhada: "))
Desconto = float(input("Digite o valor do desconto: "))
Dependentes = int(input("Digite o número de dependentes: "))

SalarioBruto = Horas * ValorHora
SalarioLiquido = (SalarioBruto - (Desconto/100)) + (Dependentes * 100)

print("O valor do seu salário líquido é: ", SalarioLiquido)
