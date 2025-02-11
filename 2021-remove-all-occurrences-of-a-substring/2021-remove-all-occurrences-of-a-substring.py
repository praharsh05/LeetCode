class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Variable for stack
        res = []
        # Variable for target length
        target_len = len(part)
        # Variable to hold the last character of the target
        target_end = part[-1]

        # Iterate over the string s and append the character into the stack
        for char in s:
            res.append(char)

            # If we reach a char which is the same as target_end and the stack is atleast 
            #as big as the target_leng then check if the last target_len characters form
            #the target, if yes then remove it from the stack
            if char == target_end and len(res) >= target_len:
                if "".join(res[-target_len:]) == part:
                    del res[-target_len:]
        
        # Convert the stack into a string and return
        return "".join(res)