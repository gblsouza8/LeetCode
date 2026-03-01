def minMoves(nums):

    # variavel contador
    contador = 0

    # variavel que irá guardar o maior valor da array
    x = nums[0]

    # encontra o maior valor da array
    for i in range(len(nums)):
        if nums[i] > x:
            x = nums[i]


    # incrementa no contador a diferença do maior numero para cada numero na array
    for i in range(len(nums)):
        if nums[i] == x:
            pass
        else:
            contador += x-nums[i]

    # retorna o contador
    return contador

nums = [2,1,3]
print(minMoves(nums))