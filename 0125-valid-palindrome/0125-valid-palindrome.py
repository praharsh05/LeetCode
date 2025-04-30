class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_string = ""

        for i in range(len(s)):
            if s[i].isalnum():
                temp_string += s[i].lower()
        
        return temp_string == temp_string[::-1]