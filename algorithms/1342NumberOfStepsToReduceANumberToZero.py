def numberOfSteps(num):

    # inicializa o contador
    contador = 0
    # enquanto num for maior que 0
    while num > 0:
        # se num for par (divisivel por 2), divide ele por 2 e incrementa o contador
        if num % 2 == 0:
            num = num/2
            contador += 1
        # se num for impar, subtrai 1 e incrementa o contador
        else:
            num = num - 1
            contador += 1
    # retorna o contador
    return contador



num = 14
print(numberOfSteps(num))