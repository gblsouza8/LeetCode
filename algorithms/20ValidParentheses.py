def isValid(s):
    lista = []
    flag = True
    rep = 0

    if len(s) == 1:
        return False
    
    if len(s) % 2 != 0:
        return False

    for i in range(len(s)):
        lista.append(s[i])



    tamanho_inicial = len(lista)
    while rep < tamanho_inicial:

        try: 
            if lista[0] == "(":
                for j in range(len(lista)):
                    if lista[j] == ")":
                        if j < len(lista)-1:
                            if lista[j+1] == "]" or lista[j+1] == "}":
                                for x in range(i, lista):
                                    if lista[x] == "[" or lista[x] == "{":
                                        for a in range(x, j):
                                            if lista[a] == "]" or lista[a] == "}":
                                                pass
                                            else:
                                                return False
                        lista.pop(j)
                        lista.pop(0)



            elif lista[0] == "{":
                for j in range(len(lista)):
                    if lista[j] == "}":
                        if j < len(lista)-1:
                            if lista[j+1] == "]" or lista[j+1] == ")":
                                for x in range(i, lista):
                                    if lista[x] == "[" or lista[x] == "(":
                                        for a in range(x, j):
                                            if lista[a] == "]" or lista[a] == ")":
                                                pass
                                            else:
                                                return False
                        lista.pop(j)
                        lista.pop(0)

            elif lista[0] == "[":
                for j in range(len(lista)):
                    if lista[j] == "]":
                        if j < len(lista)-1:
                            if lista[j+1] == ")" or lista[j+1] == "}":
                                for x in range(i, lista):
                                    if lista[x] == "(" or lista[x] == "{":
                                        for a in range(x, j):
                                            if lista[a] == ")" or lista[a] == "}":
                                                pass
                                            else:
                                                return False
                        lista.pop(j)
                        lista.pop(0)


        except:
            pass




        rep += 1


                    

                

    if len(lista) > 0:
        return False
    
    return flag








s = "()"
print(isValid(s))