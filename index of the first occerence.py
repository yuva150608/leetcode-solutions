class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len, n_len = len(haystack), len(needle)
        for i in range(h_len - n_len + 1):
            if haystack[i : i + n_len] == needle:
                return i
        return -1
