def sortSentence(s):


    # separa a string por espaços
    palavras = s.split(" ")
    # variavel que irá ser retornada após remontar a string
    saida = ""
    # laço que irá montar a string baseado na quantidade de palavras
    for i in range(1, len(palavras) + 1):
        # percorre a lista de palavras
        for j in range(0, len(palavras)):
            # se o ultimo caractere da palavra atual for igual a i
            if int(palavras[j][-1]) == i:
                # adiciona a palavra na string cortando o último caractere (numero) e adicionando um espaço no final
                saida += palavras[j][:-1] + " "
    
    # retorna a palavra sem o último espaço q apareceria
    return saida[:-1]


s = "is2 sentence4 This1 a3"
print(sortSentence(s))