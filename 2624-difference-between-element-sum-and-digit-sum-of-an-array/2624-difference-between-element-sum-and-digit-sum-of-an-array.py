class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum = sum(nums)
        dig_sum = 0
        for elem in nums:
            if elem > 9:
                for d in str(elem):
                    dig_sum += int(d)
            else:
                dig_sum += elem
        
        return abs(el_sum - dig_sum)