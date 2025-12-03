def countMatches(items, ruleKey, ruleValue):

    # variavel contador
    contador = 0

    # verifica qual o valor de ruleKey para definir a variavel x como o local onde é encontrado o valor na array
    if ruleKey == "color":
        x = 1
    elif ruleKey == "type":
        x = 0
    elif ruleKey == "name":
        x = 2

    # percorre a lista de itens
    for i in range(len(items)):
        # verifica se o indice x em cada array i é igual ao valor desejado
        if items[i][x] == ruleValue:
            # se for, incrementa o contador
            contador += 1
    # retorna o contador
    return contador






items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
print(countMatches(items, ruleKey, ruleValue))