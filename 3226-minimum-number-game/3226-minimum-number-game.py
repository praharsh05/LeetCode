class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort()
        q = deque(nums)
        while q:
            alice = q.popleft()
            bob = q.popleft()
            arr.append(bob)
            arr.append(alice)
        
        return arr