class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        prefix_sum = 0

        for num in arr:
            prefix_sum += num
            odd_count += prefix_sum % 2
        
        odd_count += (len(arr) - odd_count) * odd_count
        
        return odd_count % MOD