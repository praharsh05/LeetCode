class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        while num != 0:
            digits.append(num%10)
            num //= 10
        
        digits.sort()
        num1 = digits[0]*10 + digits[3]
        num2 = digits[1]*10 + digits[2]

        return num1 + num2