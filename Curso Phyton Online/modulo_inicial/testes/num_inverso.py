print("Insira um número abaixo que tenha três casa decimais")

num = int(input("Insira um número: "))
print(type(num))

if num < 1000 and num > 99:
    num = str(num)
    print(f"O inversao de {num} é {num [::-1]}")
    print(type(num))
else:
    print("Número Inválido")

