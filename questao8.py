'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabese que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

custo = float(input("Qual foi o valor do custo do produto?"))
percentual_venda = float(input("Qual é o percentual de venda?"))
venda = custo + (percentual_venda / 100 * custo)

print(f"Então a venda terá que ser no valor de R${venda} para se obter lucro.")