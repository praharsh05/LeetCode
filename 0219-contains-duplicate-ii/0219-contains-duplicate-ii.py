class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_num = {}

        for i, num in enumerate(nums):
            if num in hash_num:
                if abs(i - hash_num[num]) <= k:
                    return True
            hash_num[num] = i

        return False 