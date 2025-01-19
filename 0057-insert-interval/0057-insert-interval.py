class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Append the newInterval to the intervals
        intervals.append(newInterval)
        # Sort the intervals based on the start
        intervals.sort(key= lambda x: x[0])
        
        # result list to return
        res = []
        # pointer for the prev element
        prev = intervals[0]
        
        # iterate over intervals from 1 to last
        for interval in intervals[1:]:
            # Check if the end of prev is more than the start of current element
            if prev[1] >= interval[0]:
                # Make the end of prev as the max of the end of current or prev
                prev[1] = max(prev[1], interval[1])
            else:
                # Append prev to result and update prev to current element
                res.append(prev)
                prev = interval
        res.append(prev)

        return res