def findWordsContaining(words, x):
    # Inicia uma lista vazia onde salvará os indices que contém o caractere desejado
    indices = []
    # Para cada indice na lista words
    for i in range(len(words)):
        # Verifica se o caractere desejado (x) está na palavra que representa o indice atual
        if x in words[i]:
            # Se estiver, adiciona o indice na lista de indices
            indices.append(i)
    # Retorna o indice
    return indices






words = ["leet","code"]
x = "e"
print(findWordsContaining(words, x))