def sortPeople(names, heights):
    
    # lista que será montada com a ordem nova
    ordem = []

    # enquanto tiver algo em heights
    while len(heights) > 0:

        # define que maior é o indice 0
        maior = heights[0]
        # reseta a variavel indice
        indice = 0

        # percorre height
        for i in range(len(heights)):
            # se o indice atual for maior que maior, define maior como o indice atual e a variavel indice como i
            if heights[i] > maior:
                maior = heights[i]
                indice = i
        # adiciona o nome representante do maior indice em ordem
        ordem.append(names[indice])
        # deleta o indice em names e heights
        del names[indice]
        del heights[indice]

    # retorna a nova lista
    return ordem
        
names = ["Mary","John","Emma"]
heights =  [180,165,170]
print(sortPeople(names, heights))
        