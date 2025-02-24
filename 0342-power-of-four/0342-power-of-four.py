class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return log(n, 4) % 1 == 0 if n > 0 else False