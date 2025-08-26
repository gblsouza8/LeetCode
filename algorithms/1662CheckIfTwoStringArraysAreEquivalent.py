def arrayStringsAreEqual(word1, word2):

    # variaveis strings a serem comparadas
    string1 = ""
    string2 = ""

    # laço que monta a string1 usando a lista word1
    for i in range(len(word1)):
        string1 += word1[i]

    # laço que monta a string2 usando a lista word2
    for i in range(len(word2)):
        string2 += word2[i]

    # compara ambas as strings e retorna true caso sejam iguais ou false caso sejam diferentes
    if string1 == string2:
        return True
    else:
        return False

word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(arrayStringsAreEqual(word1, word2))