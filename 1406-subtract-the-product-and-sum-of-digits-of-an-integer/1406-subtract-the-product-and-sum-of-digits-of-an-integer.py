class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        string = str(n)
        prod = 1
        sumation = 0
        for digit in string:
            prod *= int(digit)
            sumation += int(digit)
        
        return prod - sumation