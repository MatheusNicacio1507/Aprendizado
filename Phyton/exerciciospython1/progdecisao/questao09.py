'''
Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

num = int(input("Insira um valor: "))

if(num > 0):
    print(f"O número {num} é positivo")
elif(num == 0):
    print(f"O número {num} é nulo")

else:
    print(f"O número {num} é negativo")