class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_a = set(nums)
        max_c = 0
        for i in set_a:
            if nums.count(i)>= len(nums)/2: return i

