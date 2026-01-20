def findThePrefixCommonArray(A, B):

    # variaveis que serão usadas
    saida = []
    contador = 0
    lista01 = []
    lista02 = []

    # percorre a lista
    for i in range(len(A)):

        # reseta o contador para 0 a cada volta
        contador = 0
        # monta duas novas listas com os indices atuais até i
        lista01.append(A[i])
        lista02.append(B[i])
        
        # percorre uma das novas listas
        for j in range(len(lista01)):
            # se encontrar o valor em ambas as listas, incrementa o contador
            if lista01[j] in lista02:
                contador += 1
        # adiciona o contador em saida
        saida.append(contador)

    # retorna saida
    return saida




A = [2,3,1]
B = [3,1,2]
print(findThePrefixCommonArray(A, B))