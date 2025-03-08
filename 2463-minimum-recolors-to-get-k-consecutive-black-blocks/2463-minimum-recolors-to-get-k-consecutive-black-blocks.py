class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = left + k
        ops = float('inf')

        while right <= len(blocks):
            count_w = 0
            for i in range(left, right):
                if blocks[i] == 'W':
                    count_w += 1
            
            ops = min(ops, count_w)
            left +=1
            right = left + k
        
        return ops