class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        count = 0

        for i, v in enumerate(s):
            if v == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    count = max(count, i-stack[-1])
                else:
                    stack.append(i)
        
        return count