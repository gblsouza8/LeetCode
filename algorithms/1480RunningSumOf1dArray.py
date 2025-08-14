def runningSum(nums):

    # lista que irá armazenar os valores somados
    lista_somada = []

    # percorre a lista de numeros
    for i in range(len(nums)):

        # define soma como 0 sempre que volta ao inicio do loop
        soma = 0

        # percorre a lista somando todos os valaores até o indice atual
        for j in range(i+1):
            soma = soma + nums[j]

        # após percorrer, adiciona a soma na lista de valores somados
        lista_somada.append(soma)


    # retorna a lista somada
    return lista_somada





nums = [1,1,1,1,1]
print(runningSum(nums))