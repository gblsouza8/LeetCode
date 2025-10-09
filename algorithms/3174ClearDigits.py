def clearDigits(s):

    # string que irá ser retornada
    string = ""
    # lista com os digitos 
    digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # lista vazia para armazenar a string e ficar mais facil de manusea-la
    lista = []
    # flag que será usada no laço while
    flag = True


    # passa o conteudo da string para a lista
    for i in range(len(s)):
        lista.append(s[i])



    # enquanto a flag for True
    while flag == True:
        # reseta i para 0 a cada volta
        i = 0
        # reseta x para False a cada volta
        x = False


        # percorre a lista
        for j in range(len(lista)):
            # se o indice atual estiver em digitos
            if lista[j] in digitos:
                # define que i terá o valor de j (indice atual)
                i = j
                # define que x é True (ainda tem digitos na lista)
                x = True
                # sai do laço que percorre a lista assim que acha o primeiro digito
                break

        # se x for False (não achou digito no laço que percorre a lista, muda a flag e termina o while)
        if x == False:
            flag = False
            break
        
        
        # se o digito atual não for o unico da lista
        if len(lista) > 1:
            # remove ele
            del lista[i]
            # remove o anterior a ele
            del lista[i-1]
        # se for o ultimo, remove apenas ele
        else:
            del lista[i]




    # monta a string usando o que sobrou da lista
    for x in range(len(lista)):
        string += lista[x]

    # retorna a string
    return string



s = "ag3"
print(clearDigits(s))