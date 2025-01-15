class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total= 0
        for i, v in enumerate(reversed(digits)):
            total += v * pow(10, i)
        
        total += 1
        res = []
        total_str = str(total)
        for i in range(len(total_str)):
            res.append(int(total_str[i]))
        
        return res
