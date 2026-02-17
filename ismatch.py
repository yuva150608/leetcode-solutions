class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == len(p): return i == len(s)

            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j+1] == '*':
                # Case 1: Skip '*' and the preceding char (0 occurrences)
                # Case 2: Use '*' if there's a match (1 or more occurrences)
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # No '*' involved, move both pointers forward
                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)
