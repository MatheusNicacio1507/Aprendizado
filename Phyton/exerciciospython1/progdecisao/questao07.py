'''
 ) Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo.
'''

num = int(input("insira um valor: "))

if(num > 0):
    print(num)

else:
    print(num * (-1))