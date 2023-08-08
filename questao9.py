'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
'''

idade = int(input("Qual é a sua idade?"))
idade_meses = 12 * idade
idade_dias = 365 * idade

print(f"Então você tem {idade} anos de vida, {idade_meses} meses de vida e {idade_dias} dias de vida.")