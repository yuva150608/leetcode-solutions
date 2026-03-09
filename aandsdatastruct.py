class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            node = node.setdefault(char, {})
        node['$'] = True # End of word marker

    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    # Try every possible child at this level
                    for child in curr:
                        if child != '$' and dfs(i + 1, curr[child]):
                            return True
                    return False
                else:
                    if char not in curr:
                        return False
                    curr = curr[char]
            return '$' in curr
        
        return dfs(0, self.trie)
