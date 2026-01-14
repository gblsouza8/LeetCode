def reversePrefix(s, k):


    # string que irá ser retornada após mudanças
    s2 = ""

    # percorre s k vezes
    for i in range(k):
        # adiciona o indice atual em s2
        s2 += s[i]
    # inverte s2
    s2 = s2[::-1]

    # adiciona o restante de s em s2
    for i in range(k, len(s)):
        s2 += s[i]
    # retorna s2
    return s2



s = "abcd"
k = 2
print(reversePrefix(s, k))