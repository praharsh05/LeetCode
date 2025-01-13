class Solution:
    def reverseWords(self, s: str) -> str:
        temp_str  = s.split(" ")
        print(temp_str)
        if '' in temp_str:
            i = 0
            flag = False
            while flag == False:
                print("word: ", temp_str[i])
                if temp_str[i] == '': 
                    temp_str.remove(temp_str[i])
                else:
                    i += 1
                if i == len(temp_str) : flag = True
        
        print(temp_str)
        res = ''
        for i in range(len(temp_str)-1, -1, -1):
            if i == 0:
                res += temp_str[i]
            else:
                res += temp_str[i] + ' '
        
        return res
