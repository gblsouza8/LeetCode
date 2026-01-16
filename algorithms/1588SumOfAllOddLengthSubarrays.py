def sumOddLengthSubarrays(arr):

    # variavel que será incrementada
    contador = 0

    # percorre a lista
    for i in range(len(arr)+1):

        # se i for impar
        if i % 2 != 0:
            # percorre a lista até o i atual
            for j in range(0, len(arr)-i +1):
                # incrementa contador
                contador += sum(arr[j:j + i])

    # retorna o contador
    return contador





arr = [1,4,2,5,3]
print(sumOddLengthSubarrays(arr))