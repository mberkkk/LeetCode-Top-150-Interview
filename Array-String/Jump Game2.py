def jump(nums):
    
    
    min_count = 0
    max_choice = 0
    
    
    for i in range(len(nums)):
        for j in range(nums[i]):
            if i + j + 1 > len(nums)-1:
                break
            else:
                if nums[i + j + 1] > max_choice:
                    max_choice = nums[i + j+1]
        i = i+ max_choice
        min_count +=1
        if i >= len(nums):
            break
        
    return min_count

nums = [2,3,1,1,4]

print(jump(nums))
        
