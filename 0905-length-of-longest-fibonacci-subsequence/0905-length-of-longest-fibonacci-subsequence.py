class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        max_len = 0
        idx_dict = {}

        for i, v in enumerate(arr):
            idx_dict[v] = i

        for i in range(1, n-1):

            start = arr[i]

            for j in range(i+1, n):

                end = arr[j]
                diff = end - start

                if diff >= start: break
                if diff in idx_dict:
                    curr = idx_dict[diff]
                    
                    dp[i][j] = dp[curr][i] + 1
                
                max_len = max(max_len, dp[i][j])
        
        return max_len if max_len > 2 else 0