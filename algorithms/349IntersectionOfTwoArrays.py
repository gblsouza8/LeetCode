def intersection(nums1, nums2):

    # lista
    iguais = []

    # procura os iguais de nums1 e nums2
    for i in range(len(nums1)):
        if nums1[i] in nums2 and nums1[i] not in iguais:
            iguais.append(nums1[i])


    # procura os iguais de nums2 e nums1
    for i in range(len(nums2)):
        if nums2[i] in nums1 and nums2[i] not in iguais:
            iguais.append(nums2[i])

    return iguais


nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))