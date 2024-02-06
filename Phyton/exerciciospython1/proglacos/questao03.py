'''
Desenvolver um programa que apresente os quadrados dos números inteiros de 15 a 200.
'''
import math

contador = 15

while(contador <= 200):
    pot = math.pow(contador,2)
    print(pot)
    contador = contador + 1