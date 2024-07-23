def plusOne(digits):
    
    r = -1
    
    if (len(digits) == 1) and digits[0] == 9:
        return [1,0]
    
    
    if (digits[-1]< 9):
        digits[-1] = digits[-1] + 1
        
    else:
        while(digits[r] == 9):
            digits[r] = 0
            r -= 1
            
            if r == (0 - len(digits)):
                if digits[r] == 9:                
                    digits[r] = 0
                    digits.append(1)
                    return digits[::-1]
                
                    
                
        
        digits[r] = digits[r] + 1
        
        
    return digits


digits = [3,4,2,1,9,9]

print(plusOne(digits))



