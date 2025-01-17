class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        hash_pat, hash_s = {}, {}

        if len(s) != len(pattern): return False

        for i in range(len(pattern)):

            if s[i] not in hash_s:
                hash_s[s[i]] = i
            
            if pattern[i] not in hash_pat:
                hash_pat[pattern[i]] = i
            
            if hash_pat[pattern[i]] != hash_s[s[i]]:
                return False
        
        return True
