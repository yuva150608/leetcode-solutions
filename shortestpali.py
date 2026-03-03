class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
            
        # Combine string with its reverse and a separator
        combined = s + "#" + s[::-1]
        
        # Standard KMP LPS (Longest Prefix Suffix) table construction
        n = len(combined)
        lps = [0] * n
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j
            
        # lps[-1] is the length of the longest palindromic prefix
        pal_len = lps[-1]
        suffix_to_reverse = s[pal_len:]
        return suffix_to_reverse[::-1] + s
