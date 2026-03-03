class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for char in columnTitle:
            # ord(char) - ord('A') + 1 converts 'A'->1, 'B'->2, ..., 'Z'->26
            current_val = ord(char) - ord('A') + 1
            ans = ans * 26 + current_val
        return ans
