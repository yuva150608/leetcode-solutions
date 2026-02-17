from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split by '.' and convert each part to an integer to remove leading zeros
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]
        
        # zip_longest fills the shorter list with 0
        for n1, n2 in zip_longest(v1, v2, fillvalue=0):
            if n1 > n2:
                return 1
            if n1 < n2:
                return -1
        return 0
