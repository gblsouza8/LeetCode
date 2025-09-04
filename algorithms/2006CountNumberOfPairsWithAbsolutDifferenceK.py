def countKDifference(nums, k):
    # inicializa o contador
    contador = 0

    # percorre nums
    for i in range(len(nums)):
        # percorre nums a partir de i
        for j in range(i, len(nums)):
            # se o arredondamento de nums[i] - nums[j] for igual a k, incrementa o contador
            if abs(nums[i] - nums[j]) == k:
                contador += 1

    # retorna o contador
    return contador




nums = [1,2,2,1]
k = 1
print(countKDifference(nums, k))