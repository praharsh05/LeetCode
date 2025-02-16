class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        pair = {}
        for i in range(len(nums)):
            if nums[i] in pair:
                count += pair[nums[i]]
            
            pair[nums[i]] = pair.get(nums[i], 0) + 1

        return count
        