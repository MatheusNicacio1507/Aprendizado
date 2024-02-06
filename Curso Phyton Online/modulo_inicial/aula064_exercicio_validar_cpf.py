"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = input("Insira o CPF: ")

# val1 = (cpf[12:13])
# val2 = (cpf[13:14])

cpf1 = (cpf [0:11])
print("CPF SEM O - : ", cpf1)
# print(f"VALIDADOR 1 = {val1} - VALIDADOR 2 = {val2}")



contador_digito1 = 10
soma = 0

for digito in cpf1:

    if digito == ".":
        pass
    else:
        digito = int(digito)
        digito_num = (digito * contador_digito1)
        contador_digito1 -= 1
        soma += digito_num

resultado_digito1 = soma * 10

digito1 = resultado_digito1 % 11

if digito1 > 9:
    print("Primeiro Dígito: ",0)
else:
    print("Primeiro Dígito: ",digito1)

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

print("CPF + o 1° Digito: ", cpf1 + str(digito1))
cpf2 = cpf1 + str(digito1)

contador_digito2 = 11
soma = 0

for digito in cpf2:

    if digito == ".":
        pass
    else:
        digito = int(digito)
        digito_num = (digito * contador_digito2)
        contador_digito2 -= 1
        soma += digito_num

resultado_digito2 = soma * 10

digito2 = resultado_digito2 % 11

if digito2 > 9:
    print("Segundo Dígito: ",0)
else:
    print("Segundo Dígito: ",digito2)

cpf_calculo = cpf1 + "-" + str(digito1) + str(digito2)

if cpf == cpf_calculo: 
    print(cpf_calculo, " é válido!")
else:
    print(cpf," é inválido!")


    





