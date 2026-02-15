def deleteGreatestValue(grid):

    # variavel que será retornada
    soma = 0

    # enquanto tiver algum indice em grid
    while True:
        if len(grid[0]) < 1:
            break

        # lista que irá guardar os maiores valores de cada linha (reseta a cada volta no while)
        lista = []

        # encontra os maiores valores de cada linha e salva na lista
        for i in range(len(grid)):
            x = grid[i][0]
            y = 0
            for j in range(len(grid[i])):
                if grid[i][j] > x:
                    x = grid[i][j]
                    y = j
            lista.append(x)
            # apaga os maiores valores em grid após adicionar na lista
            del grid[i][y]

        # encontra o maior valor que foi deletado 
        x = 0    
        for k in range(len(lista)):
            if lista[k] > x:
                x = lista[k]
        # incrementa o maior valor em soma 
        soma += x


    return soma




grid = [[10]]
print(deleteGreatestValue(grid))