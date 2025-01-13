class Solution:
    def reverseWords(self, s: str) -> str:
        temp_str  = s.split()
        print(temp_str)
        res = ''
        for i in range(len(temp_str)-1, -1, -1):
            if i == 0:
                res += temp_str[i]
            else:
                res += temp_str[i] + ' '
        
        return res
