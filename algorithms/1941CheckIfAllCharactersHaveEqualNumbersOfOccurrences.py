def areOccurrencesEqual(s):

    qtd = []
    contados = []
    for i in range(len(s)):

        if s[i] not in contados:
            soma = 0
            for j in range(len(s)):
                if s[i] == s[j]:
                    soma += 1
            qtd.append(soma)
            contados.append(s[i])

    for i in range(len(qtd)):
        for j in range(len(qtd)):
            if qtd[i] != qtd[j]:
                return False
    return True

s = "abacbc"
print(areOccurrencesEqual(s))
