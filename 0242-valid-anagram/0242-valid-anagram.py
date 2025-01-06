class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the length of both the strings are same if not return false
        if len(s) != len(t):
            return False
        #count the occurances of char in s and add that to a dict
        dicts = {}
        for c in s:
            if dicts.get(c) is not None:
                dicts[c] = dicts[c]+1
            else: 
                dicts[c] = 1
        dictt = {}
        for c in t:
            if dictt.get(c) is not None:
                dictt[c] = dictt[c]+1
            else:
                dictt[c] = 1
        if dicts == dictt: 
            return True
        else:
            return False 