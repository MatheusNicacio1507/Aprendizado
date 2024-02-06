"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte  
str -> string -> texto
Strings são textos que estão dentro de aspas
"""
print(1234)

# Aspas simples
print('Matheus Santos')
print(1, 'Matheus "Santos"') #Exibe as aspas duplas, mas precisa estar dentro de aspas simples

# Aspas duplas
print("Matheus Santos")
print(2, "Matheus 'Santos'") #Exibe as aspas simples, mas precisa estar dentro de aspas duplas

# Escape
print("Matheus \"Santos\"") #O \ ignora o caracter que vem depois dele, no ex ele ignora a ""(o \ não aparece pro usuário) 

# r
print(r"Matheus \"Santos\"") #O r ignora o \, entao ele aparece pro usuário