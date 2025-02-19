class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix = ""
        for i, v in enumerate(word):
            if v == ch:
                return v + prefix[::-1] + word[i+1:]
            prefix += v
        
        return word
