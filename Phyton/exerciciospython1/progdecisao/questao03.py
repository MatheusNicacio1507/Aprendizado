'''
Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar.
'''

num = int(input("insira um número: "))

teste = num%2

if(teste == 0):
    print("O número é par")

else:
    print("O número ímpar")