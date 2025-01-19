class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        x = intervals[0]
        for interval in intervals[1:]:
            if x[1] >= interval[0]:
                x[1] = max(x[1], interval[1])
            else:
                res.append(x)
                x = interval
        
        res.append(x)
        
        return list(res)
