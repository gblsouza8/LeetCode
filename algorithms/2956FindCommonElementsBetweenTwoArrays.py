def findIntersectionValues(nums1, nums2):

    # contadores
    contador1 = 0
    contador2 = 0
    # lista que será retornada
    saida = []

    # conta a quantidade de valores comuns em nums1 e nums2
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            contador1 += 1

    # quando sai do laço, adiciona na lista de saida
    saida.append(contador1)

    # conta a quantidade de valores comuns em nums2 e nums1
    for i in range(len(nums2)):
        if nums2[i] in nums1:
            contador2 += 1

    # quando sai do laço, adiciona na lista de saida
    saida.append(contador2)


    # retorna a saida
    return saida





nums1 = [2,3,2]
nums2 = [1,2]
print(findIntersectionValues(nums1, nums2))