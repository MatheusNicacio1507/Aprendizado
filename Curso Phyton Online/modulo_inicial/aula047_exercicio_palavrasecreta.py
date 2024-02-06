"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra = "casa"
letra_certas = " "
tentativas = 0

while True:
    letra = input("Insira uma letra da palavra: ")

    tentativas += 1

    if len(letra) > 1:
        print("Insira apenas uma letra")
        continue
    
    if letra in palavra:
      letra_certas += letra

    palavra_formada = ""
    for letra_secreta in palavra:
        if letra_secreta in letra_certas:
          palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    
    print("Palavra formada: ",palavra_formada)

    if palavra_formada == palavra:
        os.system("cls")
        print("VOCÊ GANHOU:")
        print("A palavra era ",palavra)
        print("Tentativas:", tentativas)
        letra_certas = ""
        tentativas = 0
        