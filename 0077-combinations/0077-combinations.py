class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Variable to hold the result
        res = []
        # Variable to hold the combination
        comb = []

        # Function to backtrack to get combinations
        def backtracking(start):
            # Bounding condition for when the combination reaches length of k
            if len(comb) == k:
                # Add the combination to res and return
                res.append(comb[:])
                return
            
            # Iterate from start to n+1 as n is inclusive
            for num in range(start, n+1):
                # add the number to combination
                comb.append(num)
                # Recursively call the backtracking with number + 1
                backtracking(num + 1)
                # reset the the combination for next iteration
                comb.pop()
        
        # Start backtracking from 1
        backtracking(1)

        # Return the result list
        return res
            