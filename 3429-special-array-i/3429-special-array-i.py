class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        for i in range(1, len(nums)):
            if not ((nums[i] ^ nums[i-1]) & 1): return False
        
        return True