class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0

        for word in words:
            if len(word) < len(pref): continue

            for i in range(len(pref)):
                if pref[i] != word[i]: break
                if i == len(pref) - 1: count += 1
        
        return count
