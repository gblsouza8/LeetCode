def decodeMessage(key, message):


    # lista com o alfabeto
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # lista com as letras que já apareceram na key
    aparecidas = []
    # string que irá ser retornada
    novaString2 = ""
    # monta a lista com a primeira vez que cada letra aparece na key 
    for i in range(len(key)):
        # se o caractere atual nao tiver em aparecidas e for diferente de espaço
        if key[i] not in aparecidas and key[i] != " ":
            # adiciona na lista
            aparecidas.append(key[i])
        else:
            pass


    # separa a mensagem em espaços
    message = message.split(' ')
    # percorre a mensagem
    for i in range(len(message)):
        # percorre cada caractere do indice atual de mensagem
        for j in range(len(message[i])):
            # percorre a lista de letras em key
            for x in range(len(aparecidas)):
                # se o caractere atual for igual ao indice de letras em key, adiciona o valor desse mesmo indice em alfabeto
                if message[i][j] == aparecidas[x]:
                    novaString2 += alfabeto[x]
        # coloca um espaço depois de cada indice percorrido em message
        novaString2 += " "


    # retorna a mensagem sem o ultimo caractere que seria um espaço a mais
    return novaString2[:-1]


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(decodeMessage(key, message))