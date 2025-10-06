def isAcronym(words, s):


    # flag que irá ser retornada caso nenhuma verificação seja verdadeira
    flag = True


    # se o tamanho de s e words for diferente, retorna False imediatamente
    if len(s) != len(words):
        return False

    # percorre as palavras
    for i in range(len(words)):
        # verifica se o primeiro caractere de cada palavra é diferente da letra atual em s
        if words[i][0] != s[i]:
            # se for diferente, retorna False imediatamente
            return False
        
    # se passar por todas as verificações, retorna a Flag definida como True
    return flag




words = ["an","apple"]
s = "a"
print(isAcronym(words, s))