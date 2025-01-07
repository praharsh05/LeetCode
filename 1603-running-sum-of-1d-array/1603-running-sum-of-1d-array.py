class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums2 = [0 for i in range(0, len(nums))]
        nums2[0] = nums[0]
        for i in range(1, len(nums)):
            nums2[i] = nums2[i-1] + nums[i]
        
        return nums2