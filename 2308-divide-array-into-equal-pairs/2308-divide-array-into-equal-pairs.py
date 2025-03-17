class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0: return False
        counter_freq = Counter(nums)

        for num in counter_freq:
            if counter_freq[num] % 2 != 0:
                return False
        
        return True