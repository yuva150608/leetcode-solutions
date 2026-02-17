class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Trim spaces, split into words, and return the length of the last element
        return len(s.strip().split()[-1])
