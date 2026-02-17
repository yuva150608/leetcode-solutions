class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}

        def dfs(i, j):
            # Base case: both pointers reached the end
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = False
            # Option 1: Take character from s1
            if i < len(s1) and s1[i] == s3[i + j]:
                res = dfs(i + 1, j)
            
            # Option 2: Take character from s2 (if s1 didn't work)
            if not res and j < len(s2) and s2[j] == s3[i + j]:
                res = dfs(i, j + 1)
            
            memo[(i, j)] = res
            return res

        return dfs(0, 0)
