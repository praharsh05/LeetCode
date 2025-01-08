class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums)-1
        near = far = jump = 0

        while far < goal:
            farthest_jump = 0
            for i in range(near, far+1):
                farthest_jump = max(farthest_jump, i+nums[i])

            near = far + 1
            jump +=1
            far = farthest_jump

        return jump