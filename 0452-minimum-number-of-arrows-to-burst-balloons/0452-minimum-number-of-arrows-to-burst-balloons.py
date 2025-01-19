class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)

        x = points[0]
        res = []

        for point in points[1:]:
            if x[1] >= point[0]:
                x[1] = min(x[1], point[1])
            else:
                res.append(x)
                x = point
        res.append(x)

        return len(res)
