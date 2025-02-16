class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies >= max(candies):
                res[i] = True
        
        return res