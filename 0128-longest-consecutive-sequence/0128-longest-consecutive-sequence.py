class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = list(set(nums))  # Remove duplicates
        ans = 0
        f = []  # List to store lengths of sequences
        res.sort()  # Sort unique elements
        print(res)
        for i in range(1, len(res)):
            if res[i - 1] == res[i] - 1:  # Check consecutive difference
                ans += 1
            else:
                f.append(ans)
                ans = 0
        if f:
            return max(ans + 1, max(f) + 1)
        return ans + 1
