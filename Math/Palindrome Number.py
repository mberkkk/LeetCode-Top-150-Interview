
x = -121

def isPalindrome (x):
    if x < 0:
        return False
    x = str(x)
    
    for i in range(len(x)//2):
        
        
        if x[i] != x[len(x)- i - 1]:
            return False
        
    return True


print (isPalindrome(x=x))