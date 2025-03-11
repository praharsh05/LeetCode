class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        last_idx = [-1] * 3

        for i in range(len(s)):
            last_idx[ord(s[i]) - ord('a')] = i
            if -1 not in last_idx:
                count += 1 + min(last_idx)
        
        return count