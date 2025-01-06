class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two pointer approach
        k=0
        for i in range(len(nums)):
            # If the num in the array is not equal to val, then it should be in the array
            # and we place that at the position k and then increment k
            if nums[i] != val: 
                nums[k] = nums[i]
                k+=1
        # Finally return k       
        return k
        