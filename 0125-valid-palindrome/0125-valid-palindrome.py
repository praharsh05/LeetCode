class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_string = ''
        x=0
        for y in range(len(s)):
            if (ord(s[y]) >= 97 and ord(s[y]) <= 122) \
                or (ord(s[y]) >= 48 and ord(s[y]) <= 57):
                temp_string += s[y]
            elif ord(s[y]) >= 65 and ord(s[y]) <= 90:
                temp_string += s[y].lower()
        if temp_string == temp_string[::-1]: return True
        return False