def numOfStrings(patterns, word):

    # variavel que conta as substrings
    contador = 0

    # percorre a lista de substrings
    for i in range(len(patterns)):
        # se a substring estiver na string
        if patterns[i] in word:
            # incrementa o contador
            contador += 1


    # retorna o contador
    return contador




patterns = ["a","abc","bc","d"]
word = "abc"
print(numOfStrings(patterns, word))