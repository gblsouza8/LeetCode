def minOperations(nums, k):
    contador = 0

    # percorre a lista de numeros
    for i in range(len(nums)):
        # se o numero atual for menor que k, incrementa o contador em 1
        if nums[i] < k:
            contador += 1

    # retorna a quantidade de numeros que teriam que ser removidos para que a lista tenha apenas numeros maiores
    return contador
    

    




nums = [2,11,10,1,3]
k = 10
print(minOperations(nums, k))