'''Calculadora com While'''
#####################Código de Entrada###############################
while True:
    num1 = input("Informe um número: ")
    num2 = input("Informe outro número: ")
    op = input("Informe o operador: (+ - / *): ")

    num_val = None
    num1_float = 0
    num2_float = 0
    
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_val = True
    except:
        num_val = None

    if num_val is None:
        print("Um dos números digitados é inválido.")
        continue

    op_permitidos = "+ - / *"

    if len(op) > 1:
        print("Digite apenas um operador.")
        continue
    
    if op not in op_permitidos:
        print("Operador inválido")
        continue
    #################Códido de Conta##################
   
    print("REALIZANDO SUA CONTA")

    if op == "+":
        print(f"{num1_float} + {num2_float} = ", num1_float + num2_float) 

    elif op == "-":
        print(f"{num1_float} - {num2_float} = ", num1_float - num2_float)  

    elif op == "/":
        print(f"{num1_float} / {num2_float} = ", num1_float / num2_float)  

    else:
        print(f"{num1_float} x {num2_float} = ", num1_float * num2_float)  


    #################Código de Saída##################
    sair = input("Quer sair? [s]im: ").lower().startswith("s")

    if sair is True:
        break