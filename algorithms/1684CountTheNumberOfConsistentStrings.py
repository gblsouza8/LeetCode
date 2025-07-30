def countConsistentStrings(allowed, words):
    # Define a variável x como o tamanho de palavras na lista
    x = len(words)
    # Percorre todas as palavras da lista
    for i in range(len(words)):
        # Percorre cada letra na palavra atual
        for j in range(len(words[i])):
            # Se o caractere atual da palavra não estiver na string allowed
            if words[i][j] not in allowed:
                # Diminui x em um
                x -= 1
                # Termina o laço para não verificar outros caracteres da mesma palavra
                break

    # Retorna x 
    return x



allowed = "fstqyienx"
words = ["n","eeitfns","eqqqsfs","i","feniqis","lhoa","yqyitei","sqtn","kug","z","neqqis"]
print(countConsistentStrings(allowed, words))