class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        # Backtracking
        def dfs(arr, i, vi):
            # If res array already filled
            if i >= (2*n-1):
                return True
            
            # Try each number from n to 1
            for x in range(n,0,-1):
                # Two cases:
                # x > 1, we check two places
                # x = 1, we only check one place
                # arr[i] == 0 means that index is empty
                if(x > 1 and ((not(arr[i] == 0 and (i+x < 2*n-1) and arr[i+x] == 0)) or vi[x])) or (x == 1 and (arr[i] != 0 or vi[x])):
                    continue
                
                # If a number can be placed, then place it at x and i+x index
                if x > 1:
                    arr[i] = x
                    arr[i+x] = x
                else:
                    arr[i] = x
                
                vi[x] = True

                # Find the next available index
                next_i = i+1
                while next_i < 2*n-1 and arr[next_i]:
                    next_i += 1
                
                # Place the next number
                if dfs(arr, next_i, vi): return True
                
                # Restoring the state for backtracking
                if x >1:
                    arr[i] = 0
                    arr[i+x] = 0
                else:
                    arr[i] = 0
                vi[x] = False
            
            # If no solution is found
            return False
        
        # res array to construct
        res = [0]*(2*n-1)
        # Current index
        i = 0
        # Check if we used that number
        vi = [False] * (n+1)
        # Backtracking
        dfs(res, i, vi)
        return res