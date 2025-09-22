def findMissingAndRepeatedValues(grid):

    # listas que são usadas para obter os valores
    saida = []
    indicesgrid = []
    contador = []
    numerosunicos = []
    lista = []


    # gera a lista com todos os numeros que deveriam estar no grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            indicesgrid.append(i)

    for i in range(1, len(indicesgrid)+1):
        contador.append(i)


    # cria uma lista com os numeros que estão
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            lista.append(grid[i][j])


    # encontra o numero repetido
    for i in range(len(lista)):
        if lista[i] not in numerosunicos:
            numerosunicos.append(lista[i])
        else:
            saida.append(lista[i])

    # encontra o numero que está faltando
    for i in range(len(contador)):
        if contador[i] not in lista:
            saida.append(contador[i])


    # retorna a saida
    return saida

    



grid = [[1,5,2],[8,4,3],[7,8,6]]
print(findMissingAndRepeatedValues(grid))