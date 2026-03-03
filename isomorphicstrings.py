class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
        map_t_to_s = {}
        
        for c1, c2 in zip(s, t):
            # If current characters already have a mapping, check for consistency
            if (c1 in map_s_to_t and map_s_to_t[c1] != c2) or \
               (c2 in map_t_to_s and map_t_to_s[c2] != c1):
                return False
            
            # Establish the bidirectional mapping
            map_s_to_t[c1] = c2
            map_t_to_s[c2] = c1
            
        return True
