class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s = []

        def dfs():
            nonlocal k
            if len(s) == n:
                k -= 1
                return ''.join(s) if k == 0 else ''

            for letter in 'abc':
                if not s or s[-1] != letter:
                    s.append(letter)
                    if ans:= dfs(): return ans
                    s.pop()
            
            return ''
        
        return dfs()
        