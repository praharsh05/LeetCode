class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_points = [points[i][0] for i in range(len(points))]
        diff = 0
        x_points.sort()
        for i in range(1, len(x_points)):
            if abs(x_points[i] - x_points[i-1]) > diff:
                diff = abs(x_points[i] - x_points[i-1])
        
        return diff

