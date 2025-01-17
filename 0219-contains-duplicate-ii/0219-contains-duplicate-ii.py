class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Hash map to store visited nums and indexes
        hash_num = {}

        # Iterate over nums
        for i, num in enumerate(nums):
            # Check if num in hash table and i - j <= k
            if num in hash_num and abs(i - hash_num[num]) <= k:
                return True
            # update the index in hash
            hash_num[num] = i

        return False 