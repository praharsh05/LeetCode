class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        We get a trailing zero if there are factors of 10, which is the product of 2 and 5. Sice there are always more factors of 2 than 5 in n!, number of trailing zeros is determined by number of factors of 5
        """
        count = 0
        while n > 0:
            n //= 5
            count += n
        
        return count