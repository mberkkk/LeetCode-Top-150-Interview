def solution(s1, s2):
    if len(s1) == len(s2):
        if s1[0] == s2[-1] and s1[-1] == s2[0]:  # Correct the index for the second condition
            for i in range(1, len(s1) - 1):
                if s1[i] != s2[i]:
                    return False
            return True
        return False
    else:
        return False

s1 = "bank"
s2 = "knab"

print(solution(s1, s2))
