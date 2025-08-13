def getFinalState(nums, k, multiplier):

    # repete o loop k vezes
    for i in range(k):

        # define que o menor valor é o indice 0 da lista
        min = nums[0]
        # define que x (indice que irá ser substituido na lista é 0)
        x = 0

        # percorre a lista
        for j in range(len(nums)):
            # verifica se o valor atual é menor que o valor min
            if nums[j] < min:
                # se for, substitui min pelo valor atual
                min = nums[j]
                # define que x é o indice atual
                x = j
        # após percorrer a lista toda, substitui o menor indice da lista pelo mesmo valor multiplicado pelo multiplier
        nums[x] = nums[x] * multiplier

    # retorna o novo nums
    return nums
    


nums = [2,1,3,5,6]
k = 5
multiplier = 2
print(getFinalState(nums, k, multiplier))