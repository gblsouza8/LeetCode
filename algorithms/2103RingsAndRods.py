def countPoints(rings):

    # dicionario com os rods encontrados na string e as cores em cada um
    lista = {}
    # lista pra saber quais rods ja foram encontrados na string
    japassou = []
    # contador a ser retornado
    contador = 0

    # percorre a string a partir do indice 1 (quando começa os rods) e incrementa de 2 em 2
    for i in range(1, len(rings), 2):

        # verifica se o rod atual é 0 e se ele ainda não está na lista de rods verificados
        if rings[i] == "0" and rings[i] not in japassou:
            # reseta a string
            string = ""
            # percorre a string atrás de todos os 0's
            for j in range(len(rings)):
                # quando encontra um 0
                if rings[j] == "0":
                    # adiciona na string a cor prévia a quando o rod foi encontrado
                    string += rings[j-1]
            # adiciona no dicionario a chave 0 com o valor (string) sendo as cores que foram encontradas 
            lista["0"] = string
            # adiciona 0 na lista de japassou para nao buscar as cores do 0 novamente
            japassou.append("0")


        # faz a mesma coisa que o código do 0

        elif rings[i] == "1" and rings[i] not in japassou:
            string = ""
            for j in range(len(rings)):
                if rings[j] == "1":
                    string += rings[j-1]
            lista["1"] = string
            japassou.append("1")

        elif rings[i] == "2" and rings[i] not in japassou:
            string = ""
            for j in range(len(rings)):
                if rings[j] == "2":
                    string += rings[j-1]
            lista["2"] = string
            japassou.append("2")

        elif rings[i] == "3" and rings[i] not in japassou:
            string = ""
            for j in range(len(rings)):
                if rings[j] == "3":
                    string += rings[j-1]
            lista["3"] = string
            japassou.append("3")

        elif rings[i] == "4" and rings[i] not in japassou:
            string = ""
            for j in range(len(rings)):
                if rings[j] == "4":
                    string += rings[j-1]
            lista["4"] = string
            japassou.append("4")

        elif rings[i] == "5" and rings[i] not in japassou:
            string = ""
            for j in range(len(rings)):
                if rings[j] == "5":
                    string += rings[j-1]
            lista["5"] = string
            japassou.append("5")

        elif rings[i] == "6" and rings[i] not in japassou:
            string = ""
            for j in range(len(rings)):
                if rings[j] == "6":
                    string += rings[j-1]
            lista["6"] = string
            japassou.append("6")


        elif rings[i] == "7" and rings[i] not in japassou:
            string = ""
            for j in range(len(rings)):
                if rings[j] == "7":
                    string += rings[j-1]
            lista["7"] = string
            japassou.append("7")

        elif rings[i] == "8" and rings[i] not in japassou:
            string = ""
            for j in range(len(rings)):
                if rings[j] == "8":
                    string += rings[j-1]
            lista["8"] = string
            japassou.append("8")

        elif rings[i] == "9" and rings[i] not in japassou:
            string = ""
            for j in range(len(rings)):
                if rings[j] == "9":
                    string += rings[j-1]
            lista["9"] = string
            japassou.append("9")


    # percorre os valores do dicionario 
    for valor in lista.values():
        # se encontrar as letras GBR (todas as cores) em um unico valor, incrementa o contador
        if "G" in valor and "B" in valor and "R" in valor:
            contador += 1

    # retorna o contador
    return contador






rings = "B0B6G0R6R0R6G9"
print(countPoints(rings))