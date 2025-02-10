class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(start):
            # Bounding condition for when all numbers are used
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                # Swap positions
                nums[start], nums[i] = nums[i], nums[start]
                # Recursion for next position
                backtracking(start + 1)
                # Undo swap
                nums[start], nums[i] = nums[i], nums[start]
        
        backtracking(0)
        return res

            