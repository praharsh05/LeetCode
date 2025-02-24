class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        opened = 0
        for char in s:
            if char == "(" and opened > 0:
                stack.append(char)
            if char == ")" and opened > 1:
                stack.append(char)
            opened += 1 if char == "(" else -1
        
        return "".join(stack)
