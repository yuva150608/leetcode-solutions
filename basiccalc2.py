import math

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_num = 0
        operator = '+' # Tracks the sign/op BEFORE the current number
        
        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            
            # If char is an operator or we reached the end of the string
            if char in "+-*/" or i == len(s) - 1:
                if operator == '+':
                    stack.append(curr_num)
                elif operator == '-':
                    stack.append(-curr_num)
                elif operator == '*':
                    stack.append(stack.pop() * curr_num)
                elif operator == '/':
                    # Python's // rounds down, but LeetCode requires truncation toward zero
                    top = stack.pop()
                    res = math.trunc(top / curr_num)
                    stack.append(res)
                
                operator = char
                curr_num = 0
                
        return sum(stack)
