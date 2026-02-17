import collections

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words: return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = collections.Counter(words)
        res = []
        
        # Iterate through possible starting offsets
        for i in range(word_len):
            left = i
            curr_count = collections.Counter()
            count = 0
            # Slide window by word_len increments
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_count:
                    curr_count[word] += 1
                    count += 1
                    # If word frequency exceeds allowed, shrink from left
                    while curr_count[word] > word_count[word]:
                        curr_count[s[left:left + word_len]] -= 1
                        left += word_len
                        count -= 1
                    # Valid window found
                    if count == num_words:
                        res.append(left)
                else:
                    curr_count.clear()
                    count = 0
                    left = j + word_len
        return res
