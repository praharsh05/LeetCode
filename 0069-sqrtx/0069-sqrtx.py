class Solution:
    def mySqrt(self, x: int) -> int:
        
        start = 0
        end = x

        while start <= end:
            mid = start + (end - start) // 2

            if mid * mid > x: end = mid - 1
            elif mid * mid == x: return mid
            else: start = mid + 1
        
        return end