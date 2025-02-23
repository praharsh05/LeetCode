class Solution:
    def countDigits(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        count = 0

        for d in digits:
            if num % d == 0:
                count += 1

        return count
        