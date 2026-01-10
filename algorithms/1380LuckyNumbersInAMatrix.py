def luckyNumbers(matrix):

    # variaveis que serão usadas
    colunas = []
    # atribuindo o valor de matrix em linhas só pra facilitar
    linhas = matrix
    maiores_colunas = []
    menores_linhas = []
    ambos = []

    # montando a lista colunas 
    for i in range(len(matrix[0])):
        tempLista = []
        
        for j in range(len(matrix)):
            tempLista.append(matrix[j][i])
        colunas.append(tempLista)
    

    # pegando os maiores valores de cada coluna
    for i in range(len(colunas)):
        maior = colunas[i][0]
        
        for j in range(len(colunas[i])):
            if colunas[i][j] > maior: maior = colunas[i][j]
        maiores_colunas.append(maior)

    # pegando os menores valores de cada linha
    for i in range(len(linhas)):
        menor = linhas[i][0]
        for j in range(len(linhas[i])):
            if linhas[i][j] < menor: menor = linhas[i][j]
        menores_linhas.append(menor)


    # verificando se algum valor aparece em ambos e adicionando na lista que será retornada
    for i in range(len(maiores_colunas)):
        if maiores_colunas[i] in menores_linhas:
            ambos.append(maiores_colunas[i])
    # retorna os valores que estão na lista de menores de cada linha e maiores de cada coluna
    return ambos


matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(luckyNumbers(matrix))