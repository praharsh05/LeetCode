class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = [0] * (len(prices) - 1)
        for i in range(len(prices) - 1):
            diff[i] = prices[i+1] - prices[i] if prices[i+1] - prices[i] > 0 else 0

        return sum(diff) 