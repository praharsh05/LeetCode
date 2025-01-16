from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case if t is bigger than s
        if len(s) < len(t): return ""

        # Create a dict to store char frequency in t
        char_count = defaultdict(int)
        for char in t:
            char_count[char] += 1
        
        # Variable to track remaining char in t
        target_char_remaining = len(t)
        # variable to hold the start and end index of the smallest window found
        min_window = (0, float(inf))
        # variable to hold the start index of window in s
        start_index = 0

        # Expand window
        for end_index, char in enumerate(s):
            # If char is a target char decrement the target char count
            if char_count[char] > 0:
                target_char_remaining -= 1
            # Decrement the count of char in char_count as it is a part of the window
            char_count[char] -= 1

            # Contract window
            # if current window contains all required char
            if target_char_remaining == 0:
                while True:
                    char_at_start = s[start_index]
                    # break the loop if we reach a char which is required in the window
                    if char_count[char_at_start] == 0:
                        break
                    # move the window to right
                    char_count[char_at_start] += 1
                    start_index += 1

                # Compare the window size to previous min
                if end_index - start_index < min_window[1] - min_window[0]:
                    min_window = (start_index, end_index)

                # Adjust the variables for vailidity
                char_count[s[start_index]] += 1
                target_char_remaining += 1
                start_index += 1
        
        return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1]+1]