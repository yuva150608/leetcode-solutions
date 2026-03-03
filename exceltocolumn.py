class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            # Shift to 0-indexed for modulo 26
            columnNumber -= 1
            # Get the remainder (0-25) and map to 'A'-'Z'
            remainder = columnNumber % 26
            res.append(chr(ord('A') + remainder))
            # Move to the next higher digit
            columnNumber //= 26
            
        # Reverse because we built it from right to left
        return "".join(res[::-1])
