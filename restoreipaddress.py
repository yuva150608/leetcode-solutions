class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        # Optimization: IP can't be shorter than 4 or longer than 12 digits
        if len(s) < 4 or len(s) > 12:
            return res

        def backtrack(start, path):
            # Base case: 4 segments found and all digits used
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            # Try segments of length 1, 2, or 3
            for length in range(1, 4):
                if start + length > len(s):
                    break
                
                segment = s[start : start + length]
                
                # Check segment validity: no leading zeros and value <= 255
                if (length > 1 and segment[0] == '0') or int(segment) > 255:
                    continue
                
                backtrack(start + length, path + [segment])

        backtrack(0, [])
        return res
