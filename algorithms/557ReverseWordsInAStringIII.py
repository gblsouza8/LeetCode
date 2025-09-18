def reverseWords(s):

    # monta uma lista com as palavras da string sendo separadas por espaço
    lista = s.split(" ")
    # inicia uma nova string
    novaString = ""

    # percorre as palavras
    for i in range(len(lista)):
        # percorre os caracteres da palavra atual e a escreve ao contrario na novaString
        for j in range(len(lista[i]) -1, -1, -1):
            novaString += lista[i][j]
        
        # depois de percorrer todos os caracteres, adiciona um espaço
        novaString += " "

    # retorna a novaString sem o último caractere que seria um espaço
    return novaString[:-1]




s = "Let's take LeetCode contest"
print(reverseWords(s))