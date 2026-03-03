from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Anagrams must be the same length
        if len(s) != len(t):
            return False
            
        # Step 2: Use Counter to compare character frequencies
        # This is equivalent to comparing two hash maps
        return Counter(s) == Counter(t)
