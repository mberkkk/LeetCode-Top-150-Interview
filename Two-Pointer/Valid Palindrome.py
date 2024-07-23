def isPalindrome(s):
    if (len(s) == 1):
        return True

    s = s.lower()
    alpha_list = []
    for i in s:
        if i.isalpha() or i.isdecimal():
            alpha_list.append(i)
    

    i = 0
    j = len(alpha_list)
    print(alpha_list)

    if (len(alpha_list) == 1 or len(alpha_list) == 0):
        return True

    while(alpha_list[i] == alpha_list[j-1]):
        i += 1
        j -= 1
        if i > j:
            return True
    
    return False
s = "aa"
print(isPalindrome(s))
