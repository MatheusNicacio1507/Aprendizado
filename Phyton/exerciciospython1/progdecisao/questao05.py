'''
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno.
'''

nota1 = float(input("Insira sua nota 1: "))
nota2 = float(input("Insira sua nota 2: "))
nota3 = float(input("Insira sua nota 3: "))
nota4 = float(input("Insira sua nota 4: "))

media = (nota1 + nota4 + nota3 + nota2) / 4

if(media >= 5):
    print(f"Aprovado, média: {media}")

else:
    print(f"Reprovado, média: {media}")


