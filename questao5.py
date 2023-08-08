'''
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão do primeiro pelo segundo número.
'''

num1 = float(input("Me diga num número:"))
num2 = float(input("Me diga outro número:"))

q1 = num1 + num2
q2 = num1 - num2
q3 = num2 - num1
q4 = num1 * num2
q5 = num1 / num2
q6 = num1 % num2

print(f"A soma desses dois números é: {q1:.0f}, a subtração do primeiro número pelo segundo é: {q2:.0f}, a subtração do segundo número pelo primeiro é: {q3:.0f}, o produto entre os dois números é: {q4:.0f}, a divisão do primeiro número pelo segundo é: {q5:.1f} e o resto do primeiro número pelo segundo é: {q6:.1f}.")