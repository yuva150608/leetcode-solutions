class Solution:
    def reverseWords(self, s: str) -> str:
        # split() without arguments handles all whitespace automatically
        words = s.split()
        # Reverse the list and join with a single space
        return " ".join(words[::-1])
