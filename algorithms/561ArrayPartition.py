def arrayPairSum(nums):
    # lista que irá armazenar um par temporário
    parTemp = []
    # lista com os pares
    pares = []
    # soma dos menores valores de cada par
    soma = 0

    # coloca a lista nums em ordem decrescente para facilitar a montagem dos pares
    nums.sort(reverse=True)
    # enquanto nums ainda tiver algum indice
    while len(nums) > 0:
        # reinicia parTemp
        parTemp = []
        # adiciona os 2 primeiros indices de nums em parTemp
        parTemp.append(nums[0])
        parTemp.append(nums[1])
        # adiciona parTemp em pares
        pares.append(parTemp)

        # deleta o primeiro indice de nums duas vezes (os dois numeros inseridos em pares)
        del nums[0]
        del nums[0]

    # realiza a soma do segundo indice de cada par (o menor valor de cada par)
    for i in range(len(pares)):
        soma += pares[i][1]

    # retorna a soma
    return soma

            

nums = [1,4,3,2]
print(arrayPairSum(nums))