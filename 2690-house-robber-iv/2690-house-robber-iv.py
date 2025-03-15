class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRobAtLeastK(nums, capability, k):
            count = 0
            i = 0
            
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    if count == k:
                        return True
                    i += 1
                i += 1
            return False 
        
        left = min(nums)
        right = max(nums)
        res = right

        while left <= right:
            mid = (left + right) // 2
            if canRobAtLeastK(nums, mid, k):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res