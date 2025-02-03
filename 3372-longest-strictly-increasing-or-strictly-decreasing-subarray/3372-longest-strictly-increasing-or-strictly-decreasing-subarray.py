class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Edge case when nums has only 1 element
        if len(nums) == 1: return 1
        # Variable to keep track of length of answer, increment, and decrement
        ans = 0
        inc = 1
        dec = 1

        # Iterate over nums
        for i in range(1, len(nums)):
            # For increment add 1 to inc
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1
            # For decrement add 1 to dec
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1
            # if equal let inc and dec be 1
            else:
                inc = dec = 1
            # store the max of ans, inc, dec in ans
            ans = max(ans, dec, inc)
        
        return ans