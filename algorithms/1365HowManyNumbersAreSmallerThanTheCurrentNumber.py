def smallerNumbersThanCurrent(nums):


    # lista que irá armazenar a quantidade de valores menores que cada indice
    quantidade_menores = []

    
    # percorre a lista nums
    for i in range(len(nums)):
        # define que o valor atual de x é 0, para que seja incrementado a cada numero menor encontrado
        x = 0
        # percorre a lista para comparar o indice i atual com o restante da lista
        for j in range(len(nums)):
            # se o indice i atual for maior que o indice j atual, irá incrementar x
            if nums[i] > nums[j]:
                x += 1
        # adiciona x na lista com a quantidade de valores menores
        quantidade_menores.append(x)


    # retorna a lista
    return quantidade_menores



nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))