def twoSum(numbers, target):
    j = len(numbers) -1
    k = 0
    # while(numbers[j] > target):
    #     j -=1

    for i in range(j + 1):
        if numbers[k] + numbers [j] == target:
            return [k + 1,j + 1]
        
        elif numbers[k] + numbers[j] > target:
            j -=1

        else:
            k += 1

    return -1


numbers = [-5,-3,-1,3,4]
target = -4

print(twoSum(numbers,target))