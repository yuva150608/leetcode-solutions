class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # isPal[i][j] is True if s[i..j] is a palindrome
        isPal = [[True] * n for _ in range(n)]
        # dp[i] is the min cuts for s[0..i]
        dp = [n] * n

        # Phase 1: Precompute all palindromes
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                isPal[i][j] = s[i] == s[j] and (length == 2 or isPal[i + 1][j - 1])

        # Phase 2: Compute minimum cuts
        for i in range(n):
            if isPal[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if isPal[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
