class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        int_str = [int(s, 2) for s in nums]
        int_str.sort()
        for i in range(len(int_str)+1):
            if i not in int_str: return bin(i)[2:].zfill(n)