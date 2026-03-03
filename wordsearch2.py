class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. Build the Trie
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = w
            
        res = []
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c, node):
            char = board[r][c]
            curr_node = node.children.get(char)
            
            if not curr_node:
                return
            
            # Found a word?
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None # Prevent duplicate entries
            
            # Mark visited
            board[r][c] = "#"
            
            # Explore neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    backtrack(nr, nc, curr_node)
            
            # Restore cell (Backtrack)
            board[r][c] = char

        # 2. Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, root)
                
        return res
