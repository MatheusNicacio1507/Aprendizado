'''
Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

num = int(input("insira um número: "))

div5 = num % 5
div4 = num % 4

if(div4 == 0 and div5 == 0):
    print("O número é divisível por 5 e 4")

else:
    print("O número não é divisível por 4 e 5")