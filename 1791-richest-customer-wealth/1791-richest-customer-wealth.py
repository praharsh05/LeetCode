class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for i in range(0, len(accounts)):
            sum_j = 0
            for j in range(0, len(accounts[i])):
                sum_j += accounts[i][j]
            if sum_j > maxi: maxi = sum_j
        
        return maxi