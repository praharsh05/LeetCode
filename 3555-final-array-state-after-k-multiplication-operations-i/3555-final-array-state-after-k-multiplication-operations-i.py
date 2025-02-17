class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            mini_idx = nums.index(min(nums))
            nums[mini_idx] *= multiplier

        return nums 