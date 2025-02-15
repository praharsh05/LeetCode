class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search
        left = 0
        right = len(nums)
        mid = (left + right)//2
        while right > left:
            if nums[mid] == target: return mid
            elif nums[mid] < target:
                left = mid + 1
                mid = (left + right)//2
            elif nums[mid] > target:
                right = mid
                mid = (left + right)//2
        
        return mid
