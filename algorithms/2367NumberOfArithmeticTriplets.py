def arithmeticTriplets(nums, diff):

    # variavel contador que será retornada
    contador = 0
    # percorre nums 
    for i in range(len(nums)):
        # se i for menor que o tamanho de nums -2 (garantindo que irá procurar os indices j e k)
        if i < len(nums)-2:
            # percorre nums a partir de i
            for j in range(i+1, len(nums)):
                # se nums[j] - nums[i] for igual a diferença desejada
                if nums[j] - nums[i] == diff:
                    # irá procurar o k 
                    for k in range(j+1, len(nums)):
                        # se achar a diferença novamente entre os indices k e j
                        if nums[k] - nums[j] == diff:
                            # incrementa o contador
                            contador += 1
    # retorna o contador
    return contador


nums = [4,5,6,7,8,9]
diff = 2
print(arithmeticTriplets(nums, diff))