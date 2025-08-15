def balancedStringsSplit(s):

    # lista que irá salvar as strings moldadas caractere por caractere
    lista_strings = []
    # variavel que irá ser incrementada de acordo com os pares
    pares = 0


    # monta a lista com cada indice adicionando um caractere por vez
    for i in range(1, len(s)):
        # string que é resetada a cada 
        str = ""
        # percorre a lista até o valor atual de i para montar a lista com cada indice adicionando um caractere
        for j in range(i):
            # adiciona um caractere na string i vezes
            str = str + s[j]
        # adiciona a string atual na lista
        lista_strings.append(str)


    # percorre a lista contando quantos r e quantos l tem em cada indice da lista
    for i in range(len(lista_strings)):
        # contadores que são resetados a volta no for
        r = 0
        l = 0
        for j in range(len(lista_strings[i])):
            # verifica se o caractere atual é R
            if lista_strings[i][j] == "R":
                # se for r, incrementa r
                r += 1
                # se nao for, incrementa l
            else:
                l += 1
        # se o indice atual tiver a mesma quantidade de ambos, incrementa pares
        if r == l:
            pares += 1

    # retorna a quantidade de pares + 1
    return pares+1



s = "LLLLRRRR"
print(balancedStringsSplit(s))