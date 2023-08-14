'''
Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
'''

total = int(input("Qual é o número total de Eleitores?"))
branco = int(input("Quantos votaram branco?"))
nulo = int(input("Quantos votaram nulo?"))
valido = int(input("Quantos foram válidos?"))

pb = (branco/total) *100
pn= (nulo/total) *100
pv = (valido/total) *100

print(f"Nesse munícipio,{pv}% votaram em um candidato, {pn}% votou nulo e {pb}% votou branco.")