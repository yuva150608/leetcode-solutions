class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        sign = 1
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                res += sign * num
                continue # Skip the i += 1 at the end of the loop
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                # Push the result and the sign before the parenthesis
                stack.append(res)
                stack.append(sign)
                # Reset for the expression inside the parenthesis
                res = 0
                sign = 1
            elif s[i] == ')':
                # Evaluate: previous_sign * current_res + previous_res
                res = stack.pop() * res + stack.pop()
            i += 1
        return res
