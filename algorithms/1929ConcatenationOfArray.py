def getConcatenation(nums):
    """
    Primeira solução que pensei, beats 5%
    ans = []
    for i in range(len(nums)):
        ans.append(nums[i])

    for i in range(len(nums)):
        ans.append(nums[i])

    return ans
    """

    # Segunda solução que pensei, beats 100%
    ans = []
    ans = nums + nums
    return ans

nums = [1,2,1]
print(getConcatenation(nums))






