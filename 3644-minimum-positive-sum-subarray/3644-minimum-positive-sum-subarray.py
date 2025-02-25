class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')

        for i in range(n):
            sub_sum = 0
            for j in range(i, min(i+r, n)):
                sub_sum += nums[j]

                if j-i+1 >= l and sub_sum > 0:
                    min_sum = min(min_sum, sub_sum)
        
        return min_sum if min_sum != float('inf') else -1