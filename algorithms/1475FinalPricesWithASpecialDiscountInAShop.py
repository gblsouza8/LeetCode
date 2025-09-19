def finalPrices(prices):

    # flag que irá informar caso o produto tenha um desconto válido ou nao
    valoradicionado = False
    # lista que irá ser preenchida e retornada
    saida = []

    # percorre a lista de preços
    for i in range(len(prices)):
        # define a flag como False
        valoradicionado = False
        # percorre a lista de preços a partir do preço atual
        for j in range(i+1, len(prices)):
            # se o preço[j] for menor ou igual que o preço[i], adiciona em saida, muda a flag para True e sai do laço
            if prices[j] <= prices[i]:
                saida.append(prices[i]-prices[j])
                valoradicionado = True
                break
        # se a flag não tiver sido alterada para True, não terá desconto então irá adicionar o valor normal
        if valoradicionado == False:
            saida.append(prices[i])

    # retorna a lista com os descontos
    return saida




prices = [8,4,6,2,3]
print(finalPrices(prices))