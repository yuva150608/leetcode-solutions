class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Use a set for O(1) lookups
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True # Base case: empty string
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If s[:j] is valid and s[j:i] is in the dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break # Found a valid segmentation for s[:i]
                    
        return dp[len(s)]
