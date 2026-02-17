class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # Return the valid palindromic substring
            return s[l + 1:r]

        res = ""
        for i in range(len(s)):
            # Case 1: Odd length (e.g., "aba", center is 'b')
            p1 = expand(i, i)
            # Case 2: Even length (e.g., "abba", center is between 'b's)
            p2 = expand(i, i + 1)
            # Update the longest result found so far
            res = max(res, p1, p2, key=len)
            
        return res
