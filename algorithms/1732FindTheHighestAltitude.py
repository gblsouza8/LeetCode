def largestAltitude(gain):

    # variavel que irá armazenar a soma atual de altitude
    x = 0
    # variavel que irá armazenar o maior valor
    y = 0

    # percorre a lista de ganhos
    for i in range(len(gain)):
        # soma o ganho atual com x 
        x = x + gain[i]
        # se o ganho atual for maior que y (originalmente 0), define y como x
        if x > y:
            y = x

    # retorna y dps de sair do laço
    return y


gain = [-4,-3,-2,-1,4,3,2]
print (largestAltitude(gain))