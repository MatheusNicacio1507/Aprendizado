'''
Fazer um programa que pergunte um valor em Dólares e apresente o equivalente em Reais. Considere U$1,00 =
R$3,80
'''

valor = float(input("Qual o valor (em dólar)? "))

conversao = valor * 4.70

print(f"O valor em Real é = R$ {conversao:.2f} ")