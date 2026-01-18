def maxDistinct(s):


    # lista que irá contar as diferentes possiveis letras iniciais
    letras_iniciais = []
    for i in range(len(s)):
        # se o caractere atual nao estiver em letras iniciais, adiciona na lista
        if s[i] not in letras_iniciais:
            letras_iniciais.append(s[i])
    # retorna a quantidade de indices na lista
    return len(letras_iniciais)




s = "abab"
print(maxDistinct(s))