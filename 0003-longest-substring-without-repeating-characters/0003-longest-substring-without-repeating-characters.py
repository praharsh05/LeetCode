class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set to keep track of letters
        char_in_str = set()
        # variable to keep track of longest sub string
        max_len = 0
        # variable to keep track of starting point of the string
        sptr = 0
        # loop to iterate over the string
        for i in range(len(s)):
            # if char is in set
            while s[i] in char_in_str:
                # remove char from set and move the window
                char_in_str.remove(s[sptr])
                sptr += 1
            char_in_str.add(s[i])
            max_len = max(max_len, i-sptr+1)
        
        return max_len
