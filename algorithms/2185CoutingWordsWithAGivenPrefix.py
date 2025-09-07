def prefixCount(words, pref):

    # contador que será incrementado a cada palavra com o prefixo
    contador = 0
    # flag que irá ser alterada de acordo com as verificações
    verificar = True

    # percorre a lista de palavras
    for i in range(len(words)):
        # percorre os caracteres de pref
        for j in range(len(pref)):

            # se pref for menor que a palavra atual, roda as verificações
            if len(pref) <= len(words[i]):

                # se o caractere for igual, flag continua True
                if words[i][j] == pref[j]:
                    verificar = True
                # senão, muda a flag para False e sai da palavra
                else:
                    verificar = False
                    break
            # se prefixo não for menor ou igual que a palavra, ja adiciona False e sai da palavra
            else:
                verificar = False
                break


        # se verificar sair do laço da palavra como True, incrementa o contador
        if verificar == True:
            contador += 1

    # retorna o contador
    return contador








words = ["ua","btyivy","fwofb","zptjjv","jhopih","k","pajqarpfpf","w","cdyd","ljrdthdsoa"]
pref = "owoeg"
print(prefixCount(words, pref))