class Solution:
    def isHappy(self, n: int) -> bool:
        # Set to track visited numbers
        visit = set()
        
        # func to get the next number
        def get_next_number(n):    
            output = 0
            
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            
            return output

        # loop until a cycle is detected or 1 occurs
        while n not in visit:
            visit.add(n)
            n = get_next_number(n)
            if n == 1:
                return True
        
        return False