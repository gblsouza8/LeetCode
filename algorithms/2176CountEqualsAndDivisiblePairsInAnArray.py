def countPairs(nums, k):

    # contador de pares
    pares = 0
    # percorre nums
    for i in range(len(nums)):
        # percorre nums a partir do i atual
        for j in range(i, len(nums)):
            # se i for diferente de j
            if i != j:
                # se ambos tiverem o mesmo valor
                if nums[i] == nums[j]:
                    # multiplica os indices
                    multiplicacao = abs(i * j)
                    # se a sobra da multiplicação dividida por k for 0, incrementa pares
                    if multiplicacao % k == 0:                 
                        pares += 1

    # retorna pares
    return pares



nums = [3,1,2,2,2,1,3]
k = 2
print(countPairs(nums, k))