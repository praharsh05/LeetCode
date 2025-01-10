class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = n
        i = 1

        while i < n:
            if ratings[i] == ratings[i-1]:
                i += 1
                continue
            
            curr_peak = 0
            while i < n and ratings[i] > ratings[i-1]:
                curr_peak += 1
                candies += curr_peak
                i += 1
            
            if i == n:
                return candies
            
            curr_valley = 0
            while i < n and ratings[i] < ratings[i-1]:
                curr_valley += 1
                candies += curr_valley
                i += 1

            candies -= min(curr_peak, curr_valley)
        
        return candies
