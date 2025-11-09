def findMissingElements(nums):
    # variaveis que terá o maior e o menor valor da lista
    menor = nums[0]
    maior = nums[0]
    # lista que será preenchida com os numeros esperados do menor até o maior
    numerosEsperados = []
    # lista que será preenchida com os numeros que não estão na lista
    numerosFaltantes = []

    # descobre o maior e o menor valor
    for i in range(len(nums)):
        if nums[i] > maior:
            maior = nums[i]
        elif nums[i] < menor:
            menor = nums[i]
    
    # preenche a lista de numeros esperados do menor até o maior valor
    for i in range(menor, maior+1):
        numerosEsperados.append(i)

    # procura cada numero esperado em nums
    for i in range(len(numerosEsperados)):
        # caso não encontre o numero esperado, adiciona ele em numeros faltantes
        if numerosEsperados[i] not in nums:
            numerosFaltantes.append(numerosEsperados[i])

    # retorna os numeros faltantes
    return numerosFaltantes






nums = [7,8,6,9]
print(findMissingElements(nums))