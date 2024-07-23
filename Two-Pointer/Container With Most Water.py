def maxArea(height):
    maxArea = 1
    right = len(height) - 1
    left = 0
    
    while left != right:
        maxArea = max(maxArea, (right - left) * min(height[right], height[left]))
        if height[right] < height[left]:
            right -= 1
        else:
            left += 1
    return maxArea

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
    