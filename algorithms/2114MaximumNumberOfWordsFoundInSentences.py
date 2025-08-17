def mostWordsFound(sentences):

    # define que x é a quantidade de espaços no primeiro indice de sentences, somando 1 para não ignorar a ultima palavra
    x = sentences[0].count(" ") + 1

    # percorre o restante da lista, após o indice 0 que já foi definido como x
    for i in range(1, len(sentences)):
        # se o indice atual tiver mais espaços (somando 1 para não ignorar a ultima palavra) que x
        if sentences[i].count(" ") + 1 > x:
            # define x como a quantidade do indice atual
            x = sentences[i].count(" ") + 1


    # retorna x ao sair do laço
    return x










sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
print(mostWordsFound(sentences))