class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen = set()
        res = set()
        
        # Iterate through the string, stopping 10 characters before the end
        for i in range(len(s) - 9):
            # Extract the 10-character window
            window = s[i : i + 10]
            
            # If we've seen this window before, add it to our results set
            if window in seen:
                res.add(window)
            else:
                seen.add(window)
                
        return list(res)
