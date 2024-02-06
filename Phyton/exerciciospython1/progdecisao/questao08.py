'''
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10
'''

num = int(input("Insira um valor: "))

if(num >= 1 and num <= 10):
    print(f"O {num} está na faixa de 1 a 10")
else:
    print(f"O {num} não está na faixa de 1 a 10")