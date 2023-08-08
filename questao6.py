'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final do mês.
'''

nome = input("Qual é seu nome?")
salario = float(input("Quanto que é o seu salário fixo?"))
vendas = float(input("Quanto em dinheiro você efetua por mês em vendas?"))
total = 15 / 100 * vendas + salario

print(f"Ah, então o seu nome é {nome}, o seu salário fixo é de R${salario} e o seu salário completo é de R${total:.2f}.")