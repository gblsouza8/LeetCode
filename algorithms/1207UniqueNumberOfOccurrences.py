def uniqueOccurrences(arr):

    saida = True
    numeros = []
    qtd = []

    for i in range(len(arr)):

        if arr[i] not in numeros:
            contador = 0
            for j in range(len(arr)):
                if arr[j] == arr[i]:
                    contador += 1
            numeros.append(arr[i])
            qtd.append(contador)


    for i in range(len(qtd)):

        for j in range(len(qtd)):
            if i != j:
                if qtd[i] == qtd[j]:
                    return False


    return saida





arr = [1,2]
print(uniqueOccurrences(arr))