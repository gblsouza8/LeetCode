def maximizeSum(nums, k):


    # organiza a lista em ordem decrescente
    nums = sorted(nums, reverse=True)
    # valor que será retornado
    soma = 0
    # define que x é o maior valor da array
    x = nums[0]
    # incrementa x k vezes e incrementa soma com o valor atual de x
    for i in range(k):
        soma += x
        x += 1
    # retorna soma
    return soma


nums = [1,2,3,4,5]
k = 3
print(maximizeSum(nums, k))