class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr, p_ptr = 0, 0
        star_idx, s_tmp_idx = -1, -1
        
        while s_ptr < len(s):
            # 1. Characters match or pattern has '?'
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            # 2. Pattern has '*' - record position and try matching 0 chars
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                s_tmp_idx = s_ptr
                p_ptr += 1
            # 3. Mismatch - backtrack to the last '*' found
            elif star_idx != -1:
                p_ptr = star_idx + 1
                s_tmp_idx += 1
                s_ptr = s_tmp_idx
            else:
                return False
        
        # Check if remaining characters in pattern are all '*'
        return all(x == '*' for x in p[p_ptr:])
