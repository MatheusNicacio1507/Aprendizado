'''
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro
'''

distancia = int(input("Qual a distancia a ser percorrida na viagem, em km? "))
consumo = int(input("Quantos km seu carro faz por litro? "))

print(f"Para percorrer {distancia} km, o seu aumovel usará {distancia/consumo} litros")