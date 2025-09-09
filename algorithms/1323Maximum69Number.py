def maximum69Number(num):
    # variavel para pegar a quantidade de caracteres em num e percorrer o laço
    numeros = str(num)
    # flag que verifica se o primeiro 6 a aparecer ja foi alterada
    flag = False
    # lista para montar uma nova string
    lista = []
    # string a ser retornada
    saida = ""


    # percorre os caracteres de numeros
    for i in range(len(numeros)):
        # se for 9, adiciona ele mesmo
        if numeros[i] == "9":
            lista.append(numeros[i])
        # se for 6 e a flag ainda for false, adiciona 9 e altera a flag para true
        elif numeros[i] == "6" and flag == False:
            lista.append("9")
            flag = True
        # se for 6 com a flag True, adiciona apenas 6
        else:
            lista.append("6")
            

    # adiciona todos os numeros da lista na string saida
    for i in range(len(numeros)):
        saida += lista[i]

    # retorna a string saida convertida em int
    return int(saida)





num = 9669
print(maximum69Number(num))