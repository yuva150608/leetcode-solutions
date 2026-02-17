class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Base index for calculation
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # If empty, this ')' is a new base index
                    stack.append(i)
                else:
                    # Current index minus the last index on stack
                    max_len = max(max_len, i - stack[-1])
        return max_len
