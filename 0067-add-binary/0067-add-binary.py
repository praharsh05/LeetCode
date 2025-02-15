class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        idx_a = len(a)-1
        idx_b = len(b)-1
        
        while idx_a >= 0 or idx_b >= 0 or carry == 1:
            if idx_a >= 0:
                carry += int(a[idx_a])
                idx_a -= 1
            if idx_b >= 0:
                carry += int(b[idx_b])
                idx_b -= 1
            
            res.append(str(carry % 2))
            carry //= 2
        
        return "".join(res[::-1])

        
        