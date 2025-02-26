class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeroes = len(s) - ones

        return '1' * (ones - 1) + '0' * zeroes + '1'