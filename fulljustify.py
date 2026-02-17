class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0
        for w in words:
            # Check if adding the next word exceeds maxWidth
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - num_of_letters):
                    # Use modulo to cycle through words for space distribution
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append("".join(cur))
                cur, num_of_letters = [], 0
            cur.append(w)
            num_of_letters += len(w)
            
        # Handle the last line: left-justify and pad with spaces
        res.append(" ".join(cur).ljust(maxWidth))
        return res
