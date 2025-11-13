def buildArray(nums):
    # lista que será retornada
    ans = []


    for i in range(len(nums)):
        for j in range(len(nums)):
            # se j for igual nums[i]
            if j == nums[i]:
                # adiciona nums[j] na lista
                ans.append(nums[j])

    return ans






nums = [0,2,1,5,3,4]
print(buildArray(nums))