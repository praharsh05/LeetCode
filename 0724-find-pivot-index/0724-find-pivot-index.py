class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = -1
        n= len(nums)
        if nums is None or n == 0: return pivot
        left = 0 
        right = nums[0]

        for i in range(1, n):
            right += nums[i]
        
        for i in range (n):
            right -= nums[i]
            if left == right: return i
            left += nums[i]
        
        return pivot
        