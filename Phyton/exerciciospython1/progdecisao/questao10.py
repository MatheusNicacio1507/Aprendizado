'''
Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado.
'''

num1 = int(input("Insira um valor: "))
num2 = int(input("Insira um valor: "))

div = num1 % num2

if(div == 0):
    print(f"O número {num2} é divisor de {num1}")

else:
    print(f"O número {num2} não é divisor de {num1}")