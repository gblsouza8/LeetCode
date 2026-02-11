def countOperations(num1, num2):


    # se um dos dois numeros for 0, retorna 0 imediatamente
    if num1 == 0 or num2 == 0: return 0

    # contador
    contador = 0

    # inicializa res para entrar no laço while
    res = num1+num2


    # enquanto res for maior que 0
    while res > 0:
        # se o num1 for maior ou igual que o num2
        if num1 >= num2:
            res = num1-num2
            num1 = res
            contador += 1

        # se o num2 for maior 
        else:
            res = num2-num1
            num2 = res
            contador += 1

    # retorna o contador
    return contador



num1 = 1
num2 = 0
print(countOperations(num1, num2))