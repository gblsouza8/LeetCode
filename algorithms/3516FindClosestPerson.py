def findClosest(x, y, z):

    # armazena a diferença de x e y para z em variaveis usando abs() para que o numero não fique negativo
    difx = abs(x - z)
    dify = abs(y - z)

    # se a diferença do x para z for menor que do y para z, retorna 1
    if difx < dify:
        return 1
    # se a diferença do y para z for menor que do x para z, retorna 2
    elif dify < difx:
        return 2
    # se forem iguais, retorna 0
    else:
        return 0




x = 1
y = 5
z = 3
print(findClosest(x, y, z))