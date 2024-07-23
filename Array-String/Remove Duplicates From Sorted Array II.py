def removeDuplicates(nums):
    count = 0
    temp = nums[0]
    for i in range(len(nums)):
        if nums[i] == temp:
            count +=1
        else:
            count = 1
            temp = nums[i]
        if count > 2:
            nums[i] = 99999
        
    nums.sort()
    while(nums[-1] == 99999):
        nums.pop()
    return len(nums)
nums = [1,1,1,3,4,5]
print (removeDuplicates(nums))
