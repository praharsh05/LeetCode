class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the length of both the strings are same if not return false
        if len(s) != len(t):
            return False
        #count the occurances of char in s and add that to a dict
        dict_s = {}
        for c in s:
            dict_s[c] = 1+ dict_s.get(c, 0)
        
        #count the occurances of char in t and add that to a dict
        dict_t = {}
        for c in t:
            dict_t[c] = 1+ dict_t.get(c, 0)

        # If both the dict matches then return true
        if dict_s == dict_t: 
            return True
        
        return False 