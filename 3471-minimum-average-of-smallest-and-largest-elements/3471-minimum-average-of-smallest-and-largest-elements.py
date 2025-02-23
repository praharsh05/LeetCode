class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        q = deque(nums)
        for i in range(len(nums)//2):
            averages.append((q.popleft() + q.pop())/2)
        
        return min(averages)