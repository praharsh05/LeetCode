class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 1

        left = 0
        used_bits = 0

        for right in range(n):
            while used_bits & nums[right] != 0:
                used_bits ^= nums[left]
                left += 1
            
            used_bits |= nums[right]

            max_len = max(max_len, right - left + 1)
        
        return max_len
