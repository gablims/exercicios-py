#Receba o preço atual e a média mensal de um produto, calcule e mostre o preço reajustado, sabendo-se que:
# Venda Mensal            Preço Atual         Preço       Novo 
# < 500                   < 30                +           10% 
# >= 500 e < 1000         >= 30 e < 80        +           15% 
# >= 1000                 >= 80               -           5%

# Obs.: para outras condições, preço novo será igual ao preço atual. 
#Modularizado.
#Gabriella da Silva

preco_atual = float(input("Digite o preço atual do produto: "))
media_mensal = int(input("Digite a média mensal do produto: "))

def calcReajuste ():
    if media_mensal < 500 and preco_atual < 30:
        novo_preco = preco_atual * 1.10  
    elif 500 <= media_mensal < 1000 and 30 <= preco_atual < 80:
        novo_preco = preco_atual * 1.15  
    elif media_mensal >= 1000 and preco_atual >= 80:
        novo_preco = preco_atual * 0.95  
    else:
        novo_preco = preco_atual  
    return novo_preco
print(f"O novo preço do produto é: R$ {calcReajuste():.2f}")