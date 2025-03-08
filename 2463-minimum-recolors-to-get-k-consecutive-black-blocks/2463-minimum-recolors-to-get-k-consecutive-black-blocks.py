class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        count_w = sum(1 for i in range(k) if blocks[i] == 'W')
        ops = count_w

        for right in range(k, len(blocks)):
            if blocks[right] == 'W': count_w += 1
            if blocks[left] == 'W': count_w -= 1
            left += 1
            ops = min(ops, count_w)
        
        return ops