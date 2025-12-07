def subarraySum(nums):
    n = len(nums)
    total_sum = 0
    
    for i in range(n):
        inicio = max(0, i - nums[i])
        for j in range(inicio, i + 1):
            total_sum += nums[j]
    
    return total_sum

nums = [2,3,1]
print(subarraySum(nums))