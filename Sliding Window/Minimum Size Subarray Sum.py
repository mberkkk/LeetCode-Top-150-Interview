def minSubArrayLen(target, nums):
    nums.sort(reverse= True)
    
    temp = []
    temp_target = target

    for i in range(len(nums)):
        temp.append(nums[i])
        target = target - nums[i]
        if target <= 0:
            return (temp)

    
    if target != 0:
        if len(nums) == len(temp):
            return 0
        
    return len(temp)    
    
nums = [12,28,83,4,25,26,25,2,25,25,25,12]
print(minSubArrayLen(213,nums))