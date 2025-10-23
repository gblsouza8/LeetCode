def kthCharacter(k):


    # string inicial
    word = "a"
    # string gerada
    word2 = ""
    # lista com as letras do alfabeto 
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


    # enquanto a palavra for menor que o valor desejado
    while len(word) < k:
        # reinicia a string gerada
        word2 = ""
        # percorre a palavra
        for i in range(len(word)):
            # percorre o alfabeto
            for j in range(len(alfabeto)):
                # se o caractere atual da palavra for igual ao indice atual do alfabeto
                if word[i] == alfabeto[j]:
                    # adiciona a proxima letra do alfabeto em word2
                    word2 += alfabeto[j+1]
        # junta word com word2
        word += word2


    # retorna o indice K menos 1 (porque começa em 0)
    return word[k-1]


k = 5
print(kthCharacter(k))
