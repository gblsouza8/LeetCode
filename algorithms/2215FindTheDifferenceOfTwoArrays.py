def findDifference(nums1, nums2):

    # listas que irão armazenar as diferenças
    diff1 = []
    diff2 = []

    # lista que irá ser retornada com ambas as listas de diferenças
    retorno = []

    # monta a lista de diferenças na primeira lista
    for i in range(len(nums1)):
        # se o indice atual não estiver em nums2 e nem já tiver sido inserida em diff1, adiciona em diff1
        if nums1[i] not in nums2 and nums1[i] not in diff1:
            diff1.append(nums1[i])


    # monta a segunda lista
    for i in range(len(nums2)):
        # se o indice atual não estiver em nums1 e nem já tiver sido inserida em diff2, adiciona em diff2
        if nums2[i] not in nums1 and nums2[i] not in diff2:
            diff2.append(nums2[i])
        
    # adiciona ambas as listas na lista que irá ser retornada
    retorno.append(diff1)
    retorno.append(diff2)

    # retorna a resposta
    return retorno




nums1 = [-68,-80,-19,-94,82,21,-43]
nums2 = [-63]
print(findDifference(nums1, nums2))