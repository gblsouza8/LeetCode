def countNegatives(grid):

    # contador
    contador = 0
    # percorre as listas na matrix
    for i in range(len(grid)):
        # percorre a lista i
        for j in range(len(grid[i])):
            # se o indice for menor que 0, incrementa o contador
            if grid[i][j] < 0:
                contador += 1
    # retorna o contador
    return contador





grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))