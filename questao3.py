'''
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

kg = float(input("Quantos quilos você tem?"))
altura = float(input("Quanto de altura você tem, em metros?"))
g = kg * 1000
alturacm = altura * 100

print(f"Então o seu peso em gramas é: {g:.2f}g e a sua altura em centímetos é: {alturacm:.2f}cm.")