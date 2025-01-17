class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map for keeping num and index
        hash_idx = {}
        for i, num in enumerate(nums):
            if target - num in hash_idx:
                return [i, hash_idx[target-num]]
            hash_idx[num] = i
        