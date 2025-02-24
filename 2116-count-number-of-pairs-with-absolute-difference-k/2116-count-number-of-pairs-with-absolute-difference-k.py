class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = {}
        res = 0

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num in nums:
            if num + k in count:
                res += count[num+k]
        
        return res