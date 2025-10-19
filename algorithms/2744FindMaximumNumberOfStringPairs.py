def maximumNumberOfStringPairs(words):

    # variavel que será incrementada a cada par
    contador = 0
    # percorre os indices de words
    for i in range(len(words)):
        # percorre os indices de words a partir de i
        for j in range(i, len(words)):
            # se i for diferente de j
            if i != j:
                # reverte a string atual de j
                rev = "".join(reversed(words[j]))
                # se o indice i atual for igual ao indice j invertido
                if words[i] == rev:
                    # incrementa o contador
                    contador += 1

    # retorna o contador
    return contador





words = ["cd","ac","dc","ca","zz"]
print(maximumNumberOfStringPairs(words))