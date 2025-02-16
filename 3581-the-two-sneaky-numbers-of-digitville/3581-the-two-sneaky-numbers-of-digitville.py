class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        visited = set()
        res = []
        for num in nums:
            if num in visited:
                res.append(num)
            else:
                visited.add(num)
        
        return res