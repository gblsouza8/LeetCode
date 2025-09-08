def maxDepth(s):

    # variavel que irá contar os parenteses "(" seguidos
    contador = 0
    # variavel que irá armazenar o valor maximo encontrado
    maxContador = 0

    # laço que percorre a string
    for i in range(len(s)):
        # se o caractere atual for "(" incrementa o contador
        if s[i] == "(":
            contador += 1
            # se contador for maior que o maxContador, maxContador ganhará o valor de contador
            if contador > maxContador:
                maxContador = contador
        # se o caractere atual for ")" decrementa o contador
        elif s[i] == ")":
            contador -= 1

    return maxContador




s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))