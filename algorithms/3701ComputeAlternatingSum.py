def alternatingSum(nums):
    # variavel que será retornada
    total = 0

    # percorre nums
    for i in range(len(nums)):
        # se o indice atual for par, soma em total
        if i % 2 == 0:
            total += nums[i]
        # se não for par (impar), subtrai em total
        else:
            total -= nums[i]

            
    # retorna o total
    return total






nums = [4]
print(alternatingSum(nums))