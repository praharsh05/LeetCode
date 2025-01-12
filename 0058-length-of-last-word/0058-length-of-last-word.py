class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        c = 0  # Counter for the last word length
        for char in reversed(s):  # Iterate through the string in reverse
            if char == " ":
                if c > 0:  # If we have started counting a word, stop at the next space
                    break
            else:
                c += 1  # Increment counter for characters in the word
        return c