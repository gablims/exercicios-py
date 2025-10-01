#Receba a quantidade de horas trabalhadas, o valor por hora, o percentural de desconto e o 
#número de dependentes. Calcule e mostre o salário líquido.
#Gabriella da Silva

Horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))
ValorHora = float(input("Digite o valor recebido por hora trabalhada: "))
PercentualDesconto = float(input("Digite o percentual de desconto do salário: "))
NumDependentes = int(input("Digite o número de dependentes: "))

SalarioBruto = Horas * ValorHora
SalarioLiquido = SalarioBruto - (SalarioBruto * (PercentualDesconto / 100)) + (NumDependentes * 50)

print("O salário líquido é de: ", SalarioLiquido)