class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        arr = list(s)
        l = 0
        r = len(arr) - 1

        while l < r:
            if arr[l] != arr[r]:
                if arr[l] < arr[r]: arr[r] = arr[l]
                else: arr[l] = arr[r]
            
            l += 1
            r -= 1
        
        return "".join(arr)