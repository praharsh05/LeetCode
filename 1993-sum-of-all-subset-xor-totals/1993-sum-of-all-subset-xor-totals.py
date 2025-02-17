class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(idx, curr_xor):

            if idx == len(nums): return curr_xor

            include = dfs(idx+1, curr_xor ^ nums[idx])
            exclude = dfs(idx+1, curr_xor)

            return include + exclude
        
        return dfs(0,0)
