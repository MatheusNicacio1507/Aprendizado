'''
Fazer um algoritmo que pergunte 1 número e apresente:
a) O próprio número
b) O quadrado deste número
c) A raiz quadrada deste número
'''
import math

num = int(input("Insira um número: "))

print(f"O número é {num}\nO seu quadrado é = {math.pow(num,2)}\nE sua raíz é {math.sqrt(num)}")