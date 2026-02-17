class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []

        def backtrack(start):
            # Base case: if we've reached the end of the string, add path to result
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                substring = s[start : end + 1]
                # Check if the current substring is a palindrome
                if substring == substring[::-1]:
                    path.append(substring)
                    # Recurse for the remaining part of the string
                    backtrack(end + 1)
                    # Backtrack: remove the last added substring
                    path.pop()

        backtrack(0)
        return res
