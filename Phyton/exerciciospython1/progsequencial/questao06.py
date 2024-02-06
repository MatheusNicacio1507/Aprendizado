'''
Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit, e apresente esta
temperatura convertida em graus Celsius. A fórmula da conversão é c	=	(f	–	32)	x	5	:	9	, onde c	 é a temperatura
em graus Celsius e f		em Fahrenheit.
'''

f = int(input("Insira a temperatura: "))

c = (f - 32) * 5/9

print(f"{f} graus Fahrenheit em graus Celsius é {c}")