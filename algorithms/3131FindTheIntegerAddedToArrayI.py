def addedInteger(nums1, nums2):


    # ordena as listas em ordem crescente, pois o menor valor seguirá sendo o menor valor mesmo com o incremento
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    # retorn a subtração entre ambos os menores valores
    return nums2[0] - nums1[0]







nums1 = [2,6,4]
nums2 = [9,7,5]
print(addedInteger(nums1, nums2))