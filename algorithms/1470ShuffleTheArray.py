def shuffle(nums, n):

    # listas que irão armazenar os valores
    x = []
    y = []
    # lista que irá ser montada usando as listas x e y
    retorno = []

    # monta a lista y com cada valor depois de n indices
    for i in range(int(len(nums)/2)):
        y.append(nums[i+n])

    # monta a lista x com os primeiros indices
    for i in range(int(len(nums)/2)):
        x.append(nums[i])

    # monta a lista retorno adicionando indices x seguidos de indices y
    for i in range(int(len(nums)/2)):
        retorno.append(x[i])
        retorno.append(y[i])

    # retorn a nova lista
    return retorno




nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums, n))