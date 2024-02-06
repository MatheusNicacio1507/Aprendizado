'''
 Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias
'''

valor = int(input("Qual o valor das prestações? "))
taxa = int(input("Qual o valor das taxas? "))
dia = int(input("Quantos dias está atrasado? "))

#valor	+	(valor	x	(taxa	:	100)	x	tempo

prestacao = valor + (valor * (taxa/100) * dia)

print(f"O valor da prestação com taxas vai ser de {prestacao}")
