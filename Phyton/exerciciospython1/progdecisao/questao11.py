'''
Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.
'''

num1 = int(input("Insira um número inteiro de 3 algarismos: "))

if(num1 > 99 and num1 <= 999):
    print(num1 // 100)
else:
    print("O número não tem 3 algarismos")

