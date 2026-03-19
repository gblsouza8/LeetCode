def trimTrailingVowels(s):

    # lista de vogais
    vogais = ["a", "e", "i", "o", "u"]

    # percorre a string ao contrario
    for i in range(len(s)-1, -1, -1):

        # assim que encontrar a primeira consoante, retorna a string até ela
        if s[i] not in vogais:
            return s[:i+1]
        
    # se chegar aqui, retorna uma string vazia
    return ""

s = "idea"
print(trimTrailingVowels(s))