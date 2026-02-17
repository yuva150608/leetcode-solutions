class Solution:
    def isNumber(self, s: str) -> bool:
        num, exp, dot = False, False, False
        for i, char in enumerate(s):
            if char.isdigit():
                num = True
            elif char in "+-":
                # Sign only allowed at start or immediately after 'e/E'
                if i > 0 and s[i-1] not in "eE":
                    return False
            elif char in "eE":
                # 'e/E' only allowed if digits seen and no previous 'e/E'
                if exp or not num:
                    return False
                exp, num = True, False # Reset num to ensure digits follow 'e'
            elif char == ".":
                # Dot only allowed once and not after 'e/E'
                if dot or exp:
                    return False
                dot = True
            else:
                return False
        return num
