"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1

lista = [123, "Matheus", True, False, 1.2, []]

lista[1] = "Mudei o nome de Matheus para esse texto"

print(lista[1], type(lista[1]))

print(lista) #dps de trocar