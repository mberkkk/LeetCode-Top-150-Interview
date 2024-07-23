class Solution(object):
    def isIsomorphic(self, s, t):
        s_to_t = {}
        t_to_s = {}
        for char_s, char_t in zip(s,t):
            
            if char_s not in s_to_t:
                s_to_t[char_s] = char_t
            else:
                if s_to_t[char_s] != char_t:
                    return False
                
            if char_t not in t_to_s:
                t_to_s[char_t] = char_s

            else:
                if t_to_s[char_t] != char_s:
                    return False
        
        return True
        
        
s = "badc"
t = "baba"
solution = Solution()
print(solution.isIsomorphic(s,t))
