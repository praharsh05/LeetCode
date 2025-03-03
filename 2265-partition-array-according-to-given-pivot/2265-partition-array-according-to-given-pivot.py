class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less = [num for num in nums if num < pivot]
        greater = [ num for num in nums if num > pivot]
        pivot_count = nums.count(pivot)

        return less + [pivot] * pivot_count + greater