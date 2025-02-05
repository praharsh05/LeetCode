class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == "-":
            sign = -1
            s = s[::-1]
            return sign * int(s[:len(s)-1]) if sign * int(s[:len(s)-1]) > -(2**31) else 0
        
        s = s[::-1]
        return int(s) if int(s) < 2**31 -1 else 0
