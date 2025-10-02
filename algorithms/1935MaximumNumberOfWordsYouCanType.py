def canBeTypedWords(text, brokenLetters):

    # gera uma lista com as palavras do texto separadas por espaço
    lista = text.split(" ")
    # inicializa um contador com a quantidade de palavras na lista
    contador = len(lista)
    
    # percorre a lista
    for i in range(len(lista)):

        # percorre a palavra atual da lista
        for j in range(len(lista[i])):
            # se o caractere atual estiver em brokenLetters
            if lista[i][j] in brokenLetters:
                # decrementa o contador em 1
                contador -= 1
                # sai da palavra atual
                break


    # retorna o contador
    return contador




text = "hello world"
brokenLetters = "ad"
print(canBeTypedWords(text, brokenLetters))