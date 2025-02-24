class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        d = {}

        for a, b in dominoes:
            key = min(a,b) * 10 + max(a,b)
            if key in d:
                count += d[key]
            d[key] = d.get(key, 0) + 1 
        
        return count