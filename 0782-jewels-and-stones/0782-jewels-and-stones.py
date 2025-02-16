class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        for stone in stones:
            if stone in jewels:
                total += 1
        
        return total