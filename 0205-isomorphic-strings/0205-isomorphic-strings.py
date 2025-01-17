class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Create two hash tables to store char and index of s and t
        hash_s, hash_t = {}, {}

        for i in range(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = i

            if t[i] not in hash_t:
                hash_t[t[i]] = i
            
            if hash_s[s[i]] != hash_t[t[i]]:
                return False

        return True