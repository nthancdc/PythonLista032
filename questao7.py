'''
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das prestações.
'''

valor = float(input("Me fale o valor da compra:"))
prestacao = float(input("Tem quantas prestações?"))

total = valor / prestacao

print(f"Então o valor de cada prestação será de R${total:.2f}.")