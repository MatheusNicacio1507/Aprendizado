'''
Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações.
'''

num = int(input("insira um número: "))

if(num > 20):
    print(f"{num/2}")

else:
    print(num)