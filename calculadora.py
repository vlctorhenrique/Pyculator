print("====== CALCULADORA =======")

q = 0
while q == 0:
    op = input("SELECIONE UM OPERADOR ( + | - | * | / | % ): ")
    #-------------SOMA
    if op == "+":
        n1 = int(input("Primeiro Numero:"))
        n2 = int(input("Segundo Numero:"))
        print("{} + {} = {}".format(n1, n2, n1 + n2))
    #-------------SUBTRAÇÃO
    elif op == "-":
        n1 = int(input("Primeiro Numero:"))
        n2 = int(input("Segundo Numero:"))
        print("{} - {} = {}".format(n1, n2, n1 - n2))
    #-------------MULTIPLICAÇÃO
    elif op == "*":
        n1 = int(input("Primeiro Numero:"))
        n2 = int(input("Segundo Numero:"))
        print("{} * {} = {}".format(n1, n2, n1 * n2))
    #-------------DIVISÃO
    elif op == "/":
        n1 = int(input("Digite o Numero:"))
        n2 = int(input("Digite a divizão:"))
        print("{} / {} = {}".format(n1, n2, n1/n2))
    #-------------PORCENTAGEM
    elif op == "%":
        n1 = int(input("Digite o Numero:"))
        n2 = int(input("Digite a porcentagem:"))
        print("{}% de {} é {}".format(n2, n1, (n1/100)*n2))
    q = int(input("Digite 0 para continuar ou 1 para encerrar:"))