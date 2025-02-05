class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # If less than 2 coordinates are there in the list then the answer is the those 2 points
        if len(points) <= 2: return len(points)

        # Helper function to find slope between 2 points
        def find_slope(p1: int, p2:int) -> float:
            x1, y1 = p1
            x2, y2 = p2
            # if we have a Vertical line
            if x1-x2 == 0:
                return float(inf)
            
            return (y1-y2) / (x1-x2)
        
        ans = 1
        # Iterate over all the points
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)

            for j, p2 in enumerate(points[i+1:]):
                # Find the slope between the two points
                slope = find_slope(p1, p2)
                # Add the slope in the dict
                slopes[slope] += 1
                
                ans = max(slopes[slope], ans)
        
        return ans+1