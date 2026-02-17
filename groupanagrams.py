from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map character frequency tuples to a list of strings
        res = defaultdict(list)
        
        for s in strs:
            # Create a frequency count for 'a'-'z' (26 lowercase letters)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use tuple as key because lists are not hashable in Python
            res[tuple(count)].append(s)
            
        return list(res.values())
