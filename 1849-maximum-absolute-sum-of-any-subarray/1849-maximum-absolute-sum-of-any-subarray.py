class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = 0
        max_so_far = float('-inf')
        min_so_far = float('inf')

        for num in nums:
            max_sum = max(num, max_sum + num)
            max_so_far = max(max_so_far, max_sum)

            min_sum = min(num, min_sum + num)
            min_so_far = min(min_so_far, min_sum)
        
        return max(abs(max_so_far), abs(min_so_far))