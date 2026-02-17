class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # Initialize (m+1) x (n+1) table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: an empty string t is a subsequence of any prefix of s
        for i in range(m + 1):
            dp[i][0] = 1
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, we have two choices:
                # 1. Use the character s[i-1] to match t[j-1]
                # 2. Skip the character s[i-1]
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    # If characters don't match, we must skip s[i-1]
                    dp[i][j] = dp[i-1][j]
                    
        return dp[m][n]
