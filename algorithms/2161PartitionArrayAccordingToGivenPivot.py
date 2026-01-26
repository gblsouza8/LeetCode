def pivotArray(nums, pivot):

    # listas que serão montadas para organizar a saida
    menores = []
    maiores = []
    iguais = []
    # percorre os numeros
    for i in range(len(nums)):

        # organiza em listas dependendo se é menor, maior ou igual ao pivot
        if nums[i] < pivot: 
            menores.append(nums[i])
        elif nums[i] > pivot:
            maiores.append(nums[i])
        elif nums[i] == pivot:
            iguais.append(nums[i])

    # forma a lista final concatenando as listas montadas
    lista = menores + iguais + maiores
    # retorna a lista final
    return lista


pivot = 10
nums = [9,12,5,10,14,3,10]
print(pivotArray(nums,pivot))