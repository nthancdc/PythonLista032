'''
Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor 09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta quantos minutos já se passaram desde às 00:00h deste dia.
'''

horas = int(input("Somente na unidade das horas, que horas são?"))
minutos = int(input("Quantos minutos tem a hora de agora?"))
convercao = horas * 60
resposta = convercao + minutos

print(f"Então des de 00:00, se passaram {resposta} minutos.")
