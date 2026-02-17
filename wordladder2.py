from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # 1. BFS to build the graph of shortest paths
        adj = defaultdict(list)
        levels = {beginWord: 0}
        queue = deque([beginWord])
        
        found = False
        while queue and not found:
            visited_this_level = {}
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + char + word[i+1:]
                        if next_word in wordSet:
                            # If not visited OR visited at the same level
                            if next_word not in levels or levels[next_word] == levels[word] + 1:
                                if next_word not in levels:
                                    visited_this_level[next_word] = levels[word] + 1
                                    queue.append(next_word)
                                adj[word].append(next_word)
                                if next_word == endWord:
                                    found = True
            levels.update(visited_this_level)

        # 2. DFS to reconstruct all paths
        res = []
        def dfs(word, path):
            if word == endWord:
                res.append(list(path))
                return
            if word not in adj:
                return
            for neighbor in adj[word]:
                if levels[neighbor] == levels[word] + 1:
                    path.append(neighbor)
                    dfs(neighbor, path)
                    path.pop()

        dfs(beginWord, [beginWord])
        return res
