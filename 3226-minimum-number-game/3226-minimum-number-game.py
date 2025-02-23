class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort()

        while len(nums) > 0:
            alice = nums[0]
            del nums[0]
            bob = nums[0]
            del nums[0]
            arr.append(bob)
            arr.append(alice)
        
        return arr