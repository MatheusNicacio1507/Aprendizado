"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

'''
try: 
    numero = input("Digite um número inteiro: ")
    numero = int(numero)
    if numero%2 == 0:
        print(f"O número {numero} é PAR!")
    else:
        print(f"O número {numero} é IMPAR!")
except:
    print(f"O número {numero} não é inteiro.")
'''
#------------------------------------------------------------------------------
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
hora = input("Insira as horas (inteiras): ")

try:
    hora = int(hora)

    if hora <= 23:
        if hora <= 11 and hora >= 0:
            print("Bom dia")

        elif hora <= 17:
            print("Boa Tarde")

        else:
            print("Boa Noite")
    else:
        print("Hora maior que 23.")
except:
        print(f"{hora} não é inteira")
"""
#---------------------------------------------------------------------------------
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Insira seu primeiro nome: ")

if nome:
    contagem_nome = len(nome)

    if contagem_nome <= 4:
        print("Seu nome é curto.")

    elif contagem_nome <= 6:
        print("Seu nome é normal.")

    else:
        print("Seu nome é muito grande.")

else:
    print("Você não digitou o nome")




















