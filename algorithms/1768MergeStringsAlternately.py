def mergeAlternately(word1, word2):



    # variavel que será retornada após montar a nova string
    word3 = ""


    # encontra qual palavra é a maior e define a maior como x
    x = len(word1)
    y = len(word2)
    if x > y:
        x = x
    else:
        x = y


    # laço que percorre a quantidade de letras da maior palavra
    for i in range(x):


        # se i ainda for menor que a quantidade de letras da palavra1, adiciona ela na palavra3
        if i < len(word1):
            word3 += word1[i]

        # se i ainda for menor que a quantidade de letras da palavra2, adiciona ela na palavra3
        if i < len(word2):
            word3 += word2[i]



    # retorna palavra3
    return word3






word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1, word2))