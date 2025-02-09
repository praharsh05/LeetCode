class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Compute total number of pairs which is n*(n-1)//2 where n is the lenght of nums
        n = len(nums)
        total_pairs = n * (n-1) // 2
        # use count_map to track the occurance of nums[i] - i
        count_map = defaultdict(int)
        # Set the initial good_pairs to 0
        good_pairs = 0
        
        # Iterate over nums
        for i, num in enumerate(nums):
            diff = num - i
            # increment the good pairs with the value of diff in count maps
            good_pairs += count_map[diff]
            # Increment the count_maps
            count_map[diff] += 1
        
        # total - good pairs = bad pairs
        return total_pairs - good_pairs