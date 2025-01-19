class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the points list
        points.sort(key = lambda x: x[0])

        # Variable to store the prev balloon
        prev = points[0]
        # Varibale to keep track of arrows
        arrow = 1

        # Iterate over points from the second balloon
        for point in points[1:]:
            # Check of the end of prev is after the start of the current balloon
            if prev[1] >= point[0]:
                # Set the end to be the min of ends
                prev[1] = min(prev[1], point[1])
            else:
                arrow += 1
                prev = point
        
        return arrow
