class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        diff = 0
        j = -1
        k = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]: 
                diff += 1
                if j == -1: j = i
                elif k == -1: k = i
            if diff > 2: return False
        
        if s1[j] == s2[k] and s1[k] == s2[j]:
            return True
        
        return False