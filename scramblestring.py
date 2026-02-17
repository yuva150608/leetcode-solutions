from collections import Counter
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        # Base case: strings are identical
        if s1 == s2:
            return True
        # Pruning: character frequencies must match
        if Counter(s1) != Counter(s2):
            return False
            
        n = len(s1)
        for i in range(1, n):
            # Case 1: Substrings match without swapping
            if (self.isScramble(s1[:i], s2[:i]) and 
                self.isScramble(s1[i:], s2[i:])):
                return True
            # Case 2: Substrings match after swapping
            if (self.isScramble(s1[:i], s2[n-i:]) and 
                self.isScramble(s1[i:], s2[:n-i])):
                return True
                
        return False
