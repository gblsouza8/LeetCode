def countAsterisks(s):

    # lista com os caracteres que não estão ao redor de "|"
    lista = []
    # variavel contador
    x = 0
    # flag para indicar quando abre e quando fecha um "|"
    flag = False

    # percorre a string
    for i in range(len(s)):

        # se o caractere atual for "|"
        if s[i] == "|":
            # verifica se o flag era True (já tinha sido aberto)
            if flag == True:
                # se o flag era True, muda pra false ("|" fechado)
                flag = False
            # se o flag era False, quer dizer que está abrindo agora
            else:
                # muda para True
                flag = True

        # se o caractere não for um "|"
        else:
            # verifica se o flag é False (caractere não está entre "|")
            if flag == False:
                # adiciona o caractere na lista
                lista.append(s[i])


    # percorre a lista dos caracteres
    for i in range(len(lista)):
        # se o caractere for um asteristico, incrementa x 
        if lista[i] == "*":
            x += 1
            
    # retorna x
    return x



s = "l|*e*et|c**o|*de|"
print(countAsterisks(s))