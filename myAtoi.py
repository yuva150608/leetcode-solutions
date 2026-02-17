class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() # Remove leading whitespace
        if not s: return 0
        
        sign = -1 if s[0] == '-' else 1
        if s[0] in ('-', '+'): s = s[1:]
        
        res = 0
        for char in s:
            if not char.isdigit(): break
            res = res * 10 + int(char)
            
        # Clamp the result
        res = sign * res
        return max(-2**31, min(res, 2**31 - 1))
