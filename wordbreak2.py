import functools

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict) # O(1) lookups
        
        @functools.lru_cache(None)
        def dfs(start):
            if start == len(s):
                return [""]
            
            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Get all valid sentences for the remaining suffix
                    suffixes = dfs(end)
                    for suffix in suffixes:
                        if suffix:
                            res.append(word + " " + suffix)
                        else:
                            res.append(word)
            return res
            
        return dfs(0)
