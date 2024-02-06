"""
Iterando strings com while
"""
#       012345678910
nome = 'Matheus'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)

contador = 0
nome_novo = " "

while contador < tamanho_nome:
    letra = nome[contador]
    nome_novo += f"*{letra}"
    contador += 1 

print(nome_novo)
