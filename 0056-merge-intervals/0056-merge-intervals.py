class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # result list to return
        res = []

        # Sort the intervals list based on the first element
        intervals.sort(key=lambda x: x[0])
        # Variable to keep track of the current interval
        x = intervals[0]

        # Iterate over the intervals from 1 to last
        for interval in intervals[1:]:
            # If the last element of current is >= the first element of next interval
            if x[1] >= interval[0]:
                # Set the end element to the max of end element
                x[1] = max(x[1], interval[1])
            else:
                # add the interval to the list and set x to current
                res.append(x)
                x = interval
        
        res.append(x)
        
        return list(res)
