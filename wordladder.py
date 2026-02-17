from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)]) # Store (word, level)
        
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            
            # Try all possible one-letter transformations
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + char + word[i+1:]
                    if next_word in wordSet:
                        queue.append((next_word, level + 1))
                        wordSet.remove(next_word) # Avoid revisiting
                        
        return 0
