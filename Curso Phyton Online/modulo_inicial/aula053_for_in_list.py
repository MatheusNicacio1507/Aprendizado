"""
for in com listas
"""
""""
lista = ['Maria', 'Helena', 'Luiz']
lista.append("João")
i = 0

for nome in lista:
    print(i, nome, type(nome))
    i += 1
"""
######################################

lista = ['Maria', 'Helena', 'Luiz']
lista.append("João")

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
