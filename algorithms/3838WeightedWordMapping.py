def mapWordWeights(words, weights):

    # lista com cada letra do alfabeto para comparação com weight
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # lista que irá armazenar os valores de cada string em words
    valoreswords = []
    # string que será retornada
    string = ""

    # percorre words 
    for i in range(len(words)):

        # soma reiniciada a cada volta no for
        soma = 0

        # procura cada caractere em alfabeto e incrementa soma com o indice correspondente em weights
        for j in range(len(words[i])):
            for k in range(len(alfabeto)):
                if alfabeto[k] == words[i][j]:
                    soma += weights[k]
        # adiciona soma % 26 na lista valoreswords
        valoreswords.append(soma%26)

    # inverte o alfabeto ao terminar o valor de cada palavra em words
    alfabeto = alfabeto[::-1]

    # monta a string
    for i in range(len(valoreswords)):
        string += alfabeto[valoreswords[i]]


        
    return string








words = ["abcd","def","xyz"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]
print(mapWordWeights(words, weights))