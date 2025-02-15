class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res, pos = 0,0
        for letter in reversed(columnTitle):
            digit = ord(letter) - ord("A") + 1
            res += digit * 26 ** pos
            pos += 1
        
        return res