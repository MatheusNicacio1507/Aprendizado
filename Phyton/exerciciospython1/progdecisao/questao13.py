'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente
'''

a = int(input("Insira um valor A: "))
b = int(input("Insira um valor B: "))
c = int(input("Insira um valor C: "))

if(a > b):
    aux = a
    a = b
    b = aux

if(a > c):
    aux = a
    a = c
    c = aux

if(b > c):
    aux = b
    b = c
    c = aux

print(f"Ordem crescente = {a},{b} e {c}")



