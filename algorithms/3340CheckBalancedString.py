def isBalanced(num):


    # variaveis com a soma dos indices impares e pares
    somaImpar = 0
    somaPar = 0

    # percorre os indices de num
    for i in range(len(num)):
        # se i for par, adiciona o valor em somaPar
        if i % 2 == 0:
            somaPar += int(num[i])
        # se nao for par (é impar), adiciona o valor em somaImpar
        else:
            somaImpar += int(num[i])


    # retorna True se ambos forem iguais e False se não
    if somaPar == somaImpar:
        return True
    else:
        return False
    

num = "24123"
print(isBalanced(num))


    