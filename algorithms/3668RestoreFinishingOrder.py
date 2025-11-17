def recoverOrder(order, friends):

    # lista a ser retornada
    saida = []
    # percorre order
    for i in range(len(order)):
        # se o indice atual em order estiver em friends
        if order[i] in friends:
            # adiciona em saida
            saida.append(order[i])
    # retorna saida
    return saida






order = [3,1,2,5,4]
friends = [1,3,4]
print(recoverOrder(order, friends))