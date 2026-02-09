def finalString(s):

    # string que será retornada
    s2 = ""

    # percorre os caracteres de s
    for i in range(len(s)):
        # caso o caractere seja i, inverte a string
        if s[i] == 'i':
            s2 = s2[::-1]
        # se não for i, apenas adiciona normalmente o caractere na string
        else:
            s2 = s2 + s[i]

    # retorna a string
    return s2






s = "string"
print(finalString(s))