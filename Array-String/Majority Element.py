def majorityElement(nums):
    nums.sort()
    temp = nums[0]
    count = 0
    major = -1
    max_count = -1
    for i in nums:
        if i == temp:
            count +=1
        
        else:
            if count > max_count:
                max_count = count
                major = i
            count = 1
            temp = i
        
        if count > len(nums) // 2:
            return i
        
    return major

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))