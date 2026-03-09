def minimizedStringLength(s):


    # array com os caracteres unicos
    array = []

    # adiciona cada caractere uma vez na array
    for i in range(len(s)):
        if s[i] not in array:
            array.append(s[i])

    # retorna o tamanho da array
    return len(array)






s = "aaabc"
print(minimizedStringLength(s))