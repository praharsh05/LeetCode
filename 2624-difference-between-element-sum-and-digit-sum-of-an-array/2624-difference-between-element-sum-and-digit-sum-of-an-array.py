class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element = 0
        digit = 0
        for num in nums:
            element += num
            while num > 0:
                digit += num % 10
                num //= 10
        
        return abs(element - digit)