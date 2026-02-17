class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # If character is already in the window, move the left pointer
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            
            # Update the character's last seen index
            char_map[s[right]] = right
            # Calculate current window size and update max_len
            max_len = max(max_len, right - left + 1)
            
        return max_len
