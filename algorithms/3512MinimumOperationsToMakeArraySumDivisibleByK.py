def minOperations(nums, k):
    minimo = 0
    soma = 0

    # realiza a soma dos indices da lista
    for i in range(len(nums)):
        soma += nums[i]

    # se soma já for divisivel por k, retorna o minimo imedidatamente como 0
    if soma % k == 0:
        return minimo
    

    # se soma for menor que k, retorna ela mesmo pois seria necessário chegar a 0
    if soma < k:
        return soma
    
    # decrementa a soma em 1 e soma a quantidade de operações minimas até a soma ser divisivel por k
    while True:
        soma -= 1
        minimo += 1
        if soma % k == 0:
            return minimo
    



            
nums = [3,9,7]
k = 5
print(minOperations(nums, k))