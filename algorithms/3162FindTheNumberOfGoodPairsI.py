def numberOfPairs(nums1, nums2, k):

    # variavel que irá retornar a quantidade de pares
    pares = 0

    # percorre a lista nums1
    for i in range(len(nums1)):
        # percorre a lista nums2
        for j in range(len(nums2)):
            # define que x é igual ao indice atual de nums2 multiplicado por k
            x = nums2[j] * k
            # se nums1[i] for divisivel por x, incrementa pares
            if nums1[i] % x == 0:
                pares += 1


    # retorna pares
    return pares


nums1 = [1,2,4,12]
nums2 = [2,4]
k = 3
print(numberOfPairs(nums1, nums2, k))