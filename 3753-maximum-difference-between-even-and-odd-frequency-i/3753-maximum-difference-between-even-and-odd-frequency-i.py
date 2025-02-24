class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = float('-inf')
        min_even = float('inf')

        for freq in Counter(s).values():
            if freq & 1:
                max_odd = max(max_odd, freq)
            else:
                min_even = min(min_even, freq)

        return max_odd - min_even

        

