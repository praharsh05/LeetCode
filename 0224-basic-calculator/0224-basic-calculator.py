class Solution:
    def calculate(self, s: str) -> int:
        # Variable to keep track of num, sign, resultant
        num = 0
        sign = 1
        res = 0
        # Stack Variable
        stack = []

        # Itertate over s
        for i in range(len(s)):
            # put the current element in curr
            curr = s[i]
            # if a digit is encountered
            if curr.isdigit():
                # for numbers > 9: num * 10
                num = num * 10 + int(curr)
            # Check for + -
            elif curr in '+-':
                res += num * sign
                sign = -1 if curr == '-' else 1
                num = 0
            # Check for ()
            elif curr == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif curr == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        
        return res + num * sign
        

