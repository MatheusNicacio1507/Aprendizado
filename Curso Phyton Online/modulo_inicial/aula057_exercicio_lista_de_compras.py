"""
Faça uma lista de comprar-com-listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print("Selecione uma opção")
    escolha = input("[i]nserir [a]pagar [l]istar :")

    if escolha == "i":
        os.system("cls")
        item = input("Escreva o que deseja inserir: ")
        lista.append(item)
        print("ITEM ADICIONADO!")
        print("-"*20)   

    elif escolha == "a": 
        indice = input("Insira o índice do item que deseja apagar: ")
        try:
            indice = int(indice)
            del lista[indice]
            print("ITEM APAGADO!")
            print("-"*20)

        except:
            print("ÍNDICE INVÁLIDO")
            print("-"*20)

    elif escolha == "l":
        os.system("cls")

        if len(lista) == 0:
            print("Nada para listar")
        print("-"*10)
        for i, nome in enumerate(lista):
            print(i,nome)
        print("-"*10)
    
    else:
        print("OPÇÃ INVÁLIDA")