def stableMountains(height, threshold):

    # lista que irá salvar os indices
    montanhas = []

    # laço que percorre as alturas das montanhas
    for i in range(1, len(height)):
        # se o indice anterior ao atual for maior que o threshold, 
        # irá adicionar o indice atual na lista de montanhas estaveis
        if height[i-1] > threshold:
            montanhas.append(i)
    
    # retorna a lista
    return montanhas


height = [1,2,3,4,5]
threshold = 2
print(stableMountains(height, threshold))