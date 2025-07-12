def longestCommonPrefix(strs):
    string = ""
    stringFinal = ""
    tamanho = len(strs)


    # Caso a última string da lista seja "", já finaliza e retorna o valor ""

    if len(strs[-1]) == 0:
        stringFinal = strs[-1]
        return stringFinal

    try:

        # Realiza a comparação com as duas primeiras palavras da lista para montar a string de comparação
        palavra01 = strs[0]
        palavra02 = strs[1]
        # Para evitar o erro out of index, compara o tamanho das palavras e compara utilizando o tamanho da menor
        if palavra01 > palavra02:
            for j in range(len(palavra02)):
                if palavra01[j] == palavra02[j]:
                    # Cria a string com a palavra até o indice em que elas não estão mais iguais
                    string = palavra02[:j+1]
                else:
                    # Finaliza o loop quando as palavras não são mais iguais
                    break
        else: # Caso a outra palavra seja maior:
            for j in range(len(palavra01)):
                if palavra01[j] == palavra02[j]:
                    string = palavra02[:j+1]
                else:
                    break

        # Se a string retornar um valor em branco, quer dizer que não tem nenhuma letra em comum entre as duas palavras e já retorna um valor em branco
        if string == "":
            return string



        # Se a array tiver um tamanho maior que 2, irá comparar os outros indices
        if tamanho > 2:

            # Inicia a partir do indice 2 porque o 0 e o 1 já foram utilizados na criação da string de comparação
            for i in range(2, tamanho):
                # Define a palavra atual 
                palavraAtual = strs[i]

                # Se a letra inicial da palavra atual não for igual ao da string de comparação retorna um valor em branco
                if palavraAtual[0] != string[0]:
                    stringFinal = ""
                    return stringFinal
                
                # Realiza a comparação de tamanho para evitar o out of index
                if palavraAtual > string:
                    for j in range(len(string)):
                        if palavraAtual[j] == string[j]:
                            stringFinal = string[:j+1]
                        else:
                            return stringFinal
                else:
                    for j in range(len(palavraAtual)):
                        if palavraAtual[j] == string[j]:
                            stringFinal = string[:j+1]
                        else:
                            return stringFinal

            return stringFinal
        else:
            return string




    except:
        pass

        # Se o tamanho da array for de apenas 1, o valor da string será o mesmo que ele e irá retornar o valor
        if tamanho == 1:
            string = strs[0]
            return string
        else:
            return stringFinal

    



strs = ["flower","flow","flight"]

print(((longestCommonPrefix(strs))))