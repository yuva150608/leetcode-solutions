import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Frequency of characters needed from t
        count = collections.Counter(t)
        required = len(t)
        best_left = -1
        min_length = float('inf')
        l = 0
        
        for r, char in enumerate(s):
            # Expand window to the right
            if count[char] > 0:
                required -= 1
            count[char] -= 1
            
            # When window is valid, try to contract from the left
            while required == 0:
                if r - l + 1 < min_length:
                    best_left = l
                    min_length = r - l + 1
                
                # Moving left pointer: if character was required, increment required counter
                count[s[l]] += 1
                if count[s[l]] > 0:
                    required += 1
                l += 1
                
        return "" if best_left == -1 else s[best_left : best_left + min_length]
