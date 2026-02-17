class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                board[r][c] != word[i]):
                return False
            
            # Mark the cell as visited
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore 4 directions
            res = (backtrack(r + 1, c, i + 1) or
                   backtrack(r - 1, c, i + 1) or
                   backtrack(r, c + 1, i + 1) or
                   backtrack(r, c - 1, i + 1))
            
            # Unmark the cell (backtrack)
            board[r][c] = temp
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False
