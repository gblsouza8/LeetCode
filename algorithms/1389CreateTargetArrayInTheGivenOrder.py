def createTargetArray(nums, index):

    # lista que irá ser retornada após inserir a nova lista
    saida = []

    # laço for que percorre nums
    for i in range(len(nums)):
        # insere o nums i na posição index i
        saida.insert(index[i], nums[i])
        
    # retorna a nova lista
    return saida




nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(createTargetArray(nums, index))