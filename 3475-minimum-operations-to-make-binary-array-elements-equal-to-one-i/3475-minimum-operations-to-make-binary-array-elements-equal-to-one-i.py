class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        flips = 0
        for i in range(n-2):
            if nums[i] == 0:
                for j in range(3):
                    nums[i+j] ^= 1
                flips += 1
        
        if any(num == 0 for num in nums):
            return -1
        
        return flips