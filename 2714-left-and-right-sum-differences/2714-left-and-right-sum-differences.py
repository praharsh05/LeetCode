class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

        for i in range(len(nums)):
            leftSum = sum(nums[:i])
            rightSum = sum(nums[i+1:])
            answer[i] = abs(leftSum - rightSum)
        
        return answer