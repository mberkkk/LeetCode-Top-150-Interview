class Solution(object):
    def lengthOfLongestSubstring(self, s):

        if len(s) == 0:
            return 0
        
        elif len(s) == 1:
            return 1

        print(len(s))

        r = 1
        size = -1
        tabuList = [s[0]]

        if len(s) == 2:
            if (s[r] == tabuList[0]):
                return 1
            else:
                return 2

        for l in range(len(s) -1):
            while ((tabuList.__contains__(s[r])) == False and r <= len(s) - 1):
                size = max(r - l + 1, size)
                if r != len(s) - 1:
                    tabuList.append(s[r])
                else:
                    return size
                r += 1

            tabuList.remove(s[l])

        return size

s = "pwwkew"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))