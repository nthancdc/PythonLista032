'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o valor com o acréscimo dos 10% da gorjeta do garçom.
'''

valorbruto = float(input("Quanto que foi a conta do restaurante?"))
valortotal = valorbruto + valorbruto * (10/100)

print("O valor total com o acréscimo do garçom é:",valortotal,"Reais")