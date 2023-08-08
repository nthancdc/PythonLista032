'''
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula:  IMC = peso / altura2  -  Obs: peso em quilos e altura em metros.

'''
import math

kg = float(input("Quantos quilos você tem?"))
altura = float(input("Quanto de altura você tem, em metros?"))
convercao = math.pow(altura,2)
imc = kg / convercao

print(f"Então o seu índice corporal é {imc:.2f}!")
