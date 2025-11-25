def countGoodTriplets(arr, a, b, c):

    # variavel contador que será retornado
    contador = 0
    # percorre arr
    for i in range(len(arr)):
        # percorre arr a partir do indice i
        for j in range(i+1,len(arr)):
            # se encontrar um valor que arr[i] - arr[j] for menor ou igual a a
            if abs(arr[i] - arr[j]) <= a:
                # procure o terceiro valor
                for k in range(j+1, len(arr)):
                    # se encontrar um valor que arr[j] - arr[k] for menor ou igual a b
                    if abs(arr[j] - arr[k]) <= b:
                        # verifica se arr[i] - arr[k] é menor ou igual a c
                        if abs(arr[i] - arr[k]) <= c:
                            # se passar todas as verificações, incrementa o contador
                            contador += 1


    
    return contador






arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
print(countGoodTriplets(arr, a, b, c))