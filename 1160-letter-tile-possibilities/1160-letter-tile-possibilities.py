class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def dfs(s):
            total = 0

            for char in s:
                if s[char] > 0:
                    s[char] -= 1
                    total += 1 + dfs(s)
                    s[char] += 1
            
            return total
        
        return dfs(count)