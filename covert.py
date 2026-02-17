class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        index, step = 0, 1
        
        for char in s:
            rows[index] += char
            # Change direction if at first or last row
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
            
        return "".join(rows)
